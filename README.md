# pwgen - Secure Password Generator CLI Tool

A command-line utility to generate cryptographically secure passwords with customizable length and symbols. Built with Python.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Description
`pwgen` is a CLI tool for generating secure passwords. It ensures:
- **Cryptographically safe randomness** using Python's `secrets` module.
- **Customizable password length** (default: 12 characters).
- **Optional inclusion of symbols** (e.g., `!@#$%^&*`).

## Features
- Generate passwords with specified length (`--length`).
- Include/exclude symbols (`--symbols` flag).

## Installation

```bash
git clone https://github.com/chenxing-dev/pwgen.git
cd pwgen
chmod +x pwgen.py
```

## Usage
```
pwgen [--length LENGTH] [--symbols]
```

### Arguments
- `--length`: Password length (default: `12`).
- `--symbols`: Include symbols (default: `False`).

### Examples
1. Generate a 12-character password (default):
   ```bash
   .\pwgen
   ```

2. Generate a 16-character password with symbols:
   ```bash
   .\pwgen --length 16 --symbols
   ```

3. Generate a 10-character password (no symbols):
   ```bash
   .\pwgen --length 10
   ```

## License
This project is licensed under the [MIT License](LICENSE).
