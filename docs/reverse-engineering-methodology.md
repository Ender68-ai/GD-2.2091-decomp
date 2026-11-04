# Reverse Engineering Methodology

## Tools

- Ghidra
- Geode bindings
- Cocos2d headers
- Custom analysis scripts

## Workflow

1. Import the target binary.
2. Analyze functions and references.
3. Export decompiler output.
4. Index functions and addresses.
5. Recover symbols and types.
6. Identify classes and inheritance.
7. Reconstruct individual subsystems.
8. Validate findings against binary evidence.

## Confidence Levels

- Confirmed: Directly supported by binary evidence.
- High confidence: Supported by multiple independent references.
- Inferred: Plausible interpretation.
- Unknown: Insufficient evidence.

Never present an inference as a confirmed fact.
