# Python Patterns

A collection of standalone Python programs for practicing console pattern
printing with stars, numbers, and letters.

## Project structure

```text
.
├── src/
│   └── python_pattern/
│       ├── __init__.py
│       └── *.py
├── test/
├── .gitignore
├── pyproject.toml
└── README.md
```

## Requirements

- Python 3.10 or newer

## Running a pattern

Open a terminal in the project root (`C:\WorkSpace\Python`) and run a file
with:

```powershell
python src/python_pattern/pyramidPattern.py
```

The program will ask for the number of rows.

For example, to run the butterfly pattern, use this one-line command:

```powershell
python src/python_pattern/butterflyPatter.py
```

Then enter the number of rows when prompted, for example:

```text
Enter the row size for the pattern: 5
```

Other examples:

```powershell
python src/python_pattern/plusSymbol.py
python src/python_pattern/numberPyramidPattern.py
```

If the terminal is already inside `src\python_pattern`, run:

```powershell
python butterflyPatter.py
```

## Opening and running in VS Code

Open the complete project in VS Code from PowerShell:

```powershell
code C:\WorkSpace\Python
```

To open this README directly:

```powershell
code C:\WorkSpace\Python\README.md
```

If the `code` command is unavailable, open VS Code manually and select:

```text
File → Open Folder → C:\WorkSpace\Python
```

Then open the VS Code terminal and run:

```powershell
cd C:\WorkSpace\Python
python src\python_pattern\butterflyPatter.py
```

Enter the number of rows when prompted:

```text
Enter the row size for the pattern: 5
```

## Optional editable installation

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project in editable mode:

```powershell
python -m pip install -e .
```

The source directory uses the standard `src` layout. The current examples are
standalone scripts and are intentionally run by file path.

## Validation

Compile all source files without running them:

```powershell
python -m compileall -q src
```
