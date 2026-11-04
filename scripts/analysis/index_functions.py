
import re
import csv
import json
import argparse
from pathlib import Path
from collections import Counter

FUNCTION_PATTERN = re.compile(
    r"^// Function:\s*(.*?)\s*$",
    re.MULTILINE
)

ADDRESS_PATTERN = re.compile(
    r"^// Address:\s*(.*?)\s*$",
    re.MULTILINE
)

FAILURE_PATTERN = re.compile(
    r"// DECOMPILATION FAILED\s*\n//\s*(.*)"
)

def index_functions(source: str):
    lines = source.splitlines()
    functions = []

    current = None

    for line_number, line in enumerate(lines, start=1):
        function_match = re.match(
            r"^// Function:\s*(.*?)\s*$", line
        )

        if function_match:
            if current:
                current["end_line"] = line_number - 1
                functions.append(current)

            current = {
                "name": function_match.group(1),
                "address": None,
                "status": "unknown",
                "failure_message": None,
                "start_line": line_number,
                "end_line": None,
            }

            continue

        if current is None:
            continue

        address_match = re.match(
            r"^// Address:\s*(.*?)\s*$", line
        )

        if address_match:
            current["address"] = address_match.group(1)

        if "DECOMPILATION FAILED" in line:
            current["status"] = "failed"

        elif line.strip().startswith(
            "if (" 
        ):
            pass

        # Successful decompilation is identified by the absence
        # of the failure marker when the next function begins.

    if current:
        current["end_line"] = len(lines)
        functions.append(current)

    for function in functions:
        if function["status"] == "unknown":
            function["status"] = "success"

    return functions


def main():
    parser = argparse.ArgumentParser(
        description="Index Ghidra decompilation exports."
    )

    parser.add_argument(
        "input",
        help="Path to the Ghidra-exported C++ file"
    )

    parser.add_argument(
        "--output",
        default="analysis/function-index",
        help="Output directory"
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output)

    if not input_path.is_file():
        raise SystemExit(
            f"Input file not found: {input_path}"
        )

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Reading {input_path}...")

    source = input_path.read_text(
        encoding="utf-8",
        errors="replace"
    )

    print("Indexing functions...")

    functions = index_functions(source)

    success_count = sum(
        f["status"] == "success" for f in functions
    )

    failed_count = sum(
        f["status"] == "failed" for f in functions
    )

    # JSON
    json_path = output_dir / "functions.json"

    json_path.write_text(
        json.dumps(functions, indent=2),
        encoding="utf-8"
    )

    # CSV
    csv_path = output_dir / "functions.csv"

    with csv_path.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=functions[0].keys() if functions else []
        )

        writer.writeheader()
        writer.writerows(functions)

    # Summary
    summary = f"""Geometry Dash 2.2091 Function Index

Total functions: {len(functions)}
Successful: {success_count}
Failed: {failed_count}

Input: {input_path}
"""

    (output_dir / "summary.txt").write_text(
        summary,
        encoding="utf-8"
    )

    print()
    print("Indexing complete!")
    print(f"Total: {len(functions)}")
    print(f"Successful: {success_count}")
    print(f"Failed: {failed_count}")
    print(f"Output: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
