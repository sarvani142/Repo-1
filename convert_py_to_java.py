import re
import sys
from pathlib import Path

def style_and_update_print(py_code: str, new_message: str) -> str:
    """
    Styles the Python code and updates print statements.
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

    # Replace print statements with new message
    styled_code = re.sub(r'print\((.*?)\)', f'print("{new_message}")', styled_code)

    return styled_code


def main():
    if len(sys.argv) < 3:
        print("Usage: python update_print.py <python_file> <new_message>")
        sys.exit(1)

    py_file = Path(sys.argv[1])
    new_message = sys.argv[2]

    if not py_file.exists():
        print(f"Error: {py_file} not found")
        sys.exit(1)

    py_code = py_file.read_text()
    updated_code = style_and_update_print(py_code, new_message)

    # Save the updated file (overwrite or create new file)
    output_file = py_file.with_name(py_file.stem + "_updated.py")
    output_file.write_text(updated_code)

    print(f"✅ Updated {py_file} -> {output_file}")


if __name__ == "__main__":
    main()
