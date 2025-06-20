from typing import List
import pathlib
import os

# Tree drawing symbols
VERTICAL_PREFIX = "│   "
INDENT_PREFIX = "    "
VERTICAL_LINE = "│"
END_BRANCH = "└──"
MID_BRANCH = "├──"

def build_tree(lines: List[str], path: pathlib.Path, indent: str = ""):
    items = sorted(list(path.iterdir()), key=lambda x: x.is_file())
    for idx, item in enumerate(items):
        branch = END_BRANCH if idx == len(items) - 1 else MID_BRANCH
        if item.is_dir():
            lines.append(f"{indent}{branch} {item.name}{os.sep}")
            new_indent = indent + (VERTICAL_PREFIX if branch == MID_BRANCH else INDENT_PREFIX)
            # Show ellipsis for special folders
            if item.name in {"__pycache__", ".venv"} and item.name != pathlib.Path(os.getcwd()).name:
                lines.append(f"{new_indent}{END_BRANCH} ...")
            else:
                build_tree(lines, item, new_indent)
            lines.append(VERTICAL_LINE)
        else:
            lines.append(f"{indent}{branch} {item.name}")

def create_directory_tree(root_path: pathlib.Path) -> List[str]:
    lines = [f"{root_path.name}{os.sep}", VERTICAL_LINE]
    build_tree(lines, root_path)
    return lines

if __name__ == "__main__":
    root = pathlib.Path(os.getcwd())
    for line in create_directory_tree(root):
        print(line)


