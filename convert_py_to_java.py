import re
import sys
from pathlib import Path

def style_python_code(py_code: str) -> str:
    """
    Very naive Python code styler.
    Adjusts indentation, comments, and spacing for readability.
    """
    styled_code = py_code

    # Standardize indentation (4 spaces)
    styled_code = styled_code.replace("\t", "    ")

    # Ensure space after commas
    styled_code = re.sub(r',(\S)', r', \1', styled_code)

    # Standardize comments with a space after #
    styled_code = re.sub(r'#(\S)', r'# \1', styled_code)

    # Ensure single blank line between functions
    styled_code = re.sub(r'\n{2,}def', r'\n\ndef', styled_code)

    return styled_code


def main():
    if len(sys.argv) < 2:
        print("Usage: python style_python.py <python_file>")
        sys.exit(1)

    py_file = Path(sys.argv[1])
    if not py_file.exists():
        print(f"Error: {py_file} not found")
        sys.exit(1)

    py_code = py_file.read_text()
    styled_code = style_python_code(py_code)

    output_file = py_file.with_name(py_file.stem + "_styled._
