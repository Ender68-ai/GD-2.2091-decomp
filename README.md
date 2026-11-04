# Geometry Dash 2.2091 Decompiled

An independent reverse-engineering and reconstruction project
for Geometry Dash 2.2091 (Windows x86-64).

The goal is to analyze the game's internal architecture and
produce an organized, readable C++ reconstruction.

## Target

| Property | Value |
|---|---|
| Game | Geometry Dash |
| Version | 2.2091 |
| Platform | Windows |
| Architecture | x86-64 |
| Analysis tool | Ghidra |
| Language | C++ |

## Project Status

- [x] Import GeometryDash.exe into Ghidra
- [x] Initial function decompilation export
- [ ] Function indexing
- [ ] Symbol and class identification
- [ ] Type recovery
- [ ] Class reconstruction
- [ ] Subsystem reconstruction
- [ ] Behavioral verification

## Repository Structure

- `GD/` - Geometry Dash-specific reconstruction.
- `Cocos2d/` - Cocos2d-related reconstruction.
- `Extensions/` - Additional engine extensions.
- `bindings/` - Reference bindings and symbol information.
- `analysis/` - Reverse-engineering data.
- `scripts/` - Automation and analysis scripts.
- `docs/` - Documentation and discoveries.
- `tests/` - Validation tests.

## Reconstruction Status

This project distinguishes between:

- **Decompiled:** Direct output from Ghidra.
- **Reconstructed:** Organized and cleaned-up code.
- **Verified:** Confirmed against reliable binary evidence.

## Important

This is not the original Geometry Dash source code.

Decompiler output is approximate C-like pseudocode. Original
comments, formatting, variable names, and some type information
cannot be reliably recovered.

Reconstructed code may not compile or reproduce the original
behavior without additional work.

## Legal Notice

Geometry Dash and its associated trademarks belong to their
respective owners.

This project is independently maintained for research and
educational purposes. Do not distribute proprietary game binaries,
game assets, or other copyrighted material without authorization.
