# Directory Tree Generator

This Python script generates a visual representation of a directory structure in a tree-like format, similar to the `tree` command in Unix-like systems. It uses Unicode characters to create a hierarchical view of files and directories, making it easy to understand the organization of a project or folder.

## Features
- Recursively traverses a directory and its subdirectories.
- Sorts items alphabetically, prioritizing directories over files.
- Displays directories and files with appropriate tree-like symbols (`├──`, `└──`, `│`).
- Omits detailed contents of special folders like `__pycache__` and `.venv`, showing an ellipsis (`...`) instead.
- Uses the `pathlib` library for cross-platform path handling.

## Usage
Run the script from the command line in the directory you want to visualize:

```bash
python directory_tree.py
```

The script will print the directory structure starting from the current working directory.

## Code Explanation
- **Dependencies**: Requires `pathlib` and `os` from the Python standard library.
- **Main Functions**:
  - `build_tree(lines: List[str], path: pathlib.Path, indent: str)`: Recursively builds the tree by iterating through directory contents and appending formatted lines.
  - `create_directory_tree(root_path: pathlib.Path) -> List[str]`: Initializes the tree with the root directory and calls `build_tree` to generate the full structure.
- **Special Handling**: Skips detailed listing for `__pycache__` and `.venv` folders to keep the output clean.
- **Output**: Returns a list of strings representing the tree, which is then printed line by line.

## Example Output
For a directory structure like:
```
project/
├── data/
│   └── file.txt
├── src/
│   └── main.py
└── Readme.md
```

Running the script will produce:
```
project/
│
├── data/
│   └── file.txt
│
├── src/
│   └── main.py
│
└── Readme.md
│
```

## Requirements
- Python 3.6+
- No external dependencies

## Notes
- The script is designed to be lightweight and portable, using only standard library modules.
- It sorts items to ensure consistent output, with directories listed before files.
- The output is purely text-based and can be redirected to a file for documentation purposes (e.g., `python directory_tree.py > tree.txt`).
