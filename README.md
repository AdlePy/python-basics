# Python Basics

Topic-based Python practice scripts covering core syntax, data structures, functions, file handling, paths, and basic PyQt6 GUI examples.

## Requirements

- Python 3.14+
- Optional: `uv` for dependency management

## Setup

### Option 1: Use `uv` (recommended)

```bash
uv sync
```

### Option 2: Use `venv` + `pip`

```bash
python -m venv .venv
```

Activate the virtual environment:

- Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

- macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install pyqt6
```

## Run Examples

Each folder has an executable script. Run from the project root:

```bash
python hello-world/main.py
python base-types/main.py
python control-flows/main.py
python cycles/main.py
python data-structures/main.py
python functions/main.py
python functools_itertools/main_itertools.py
python functools_itertools/main_functools.py
python files/main_txt.py
python files/main_json.py
python files/main_csv.py
python files/config_main.py
python os_paths/os_module.py
python os_paths/pathlib_module.py
python gui-app/main.py
python gui-app/timer.py
```

## Project Layout

```text
python-basics/
|-- hello-world/            # first hello world script
|-- base-types/             # numeric, string, bool basics
|-- control-flows/          # if / elif / else examples
|-- cycles/                 # for/while loops, break/continue
|-- data-structures/        # tuple, list, dict, set, comprehensions
|-- functions/              # function args, *args, **kwargs, lambda/map/filter
|-- functools_itertools/    # reduce, lru_cache, partial, itertools tools
|-- files/                  # txt/json/csv/configparser read-write demos
|-- os_paths/               # os and pathlib path/file operations
|-- gui-app/                # PyQt6 hello window and timer app
|-- pyproject.toml
|-- uv.lock
`-- README.md
```

## Notes

- Some scripts write to local sample files (`files/` and `os_paths/file.txt`).
- `gui-app` examples require `PyQt6`.
