import re
import sys
from pathlib import Path

def convert_python_to_java(py_code: str) -> str:
    """
    Very naive Python -> Java converter.
    Handles only simple cases for demo purposes.
    """
    java_code = py_code

    # Replace print statements
    java_code = re.sub(r'print\((.*)\)', r'System.out.println(\1);', java_code)

    # Replace def functions with public static methods
    java_code = re.sub(r'def (\w+)\((.*?)\):',
                       r'public static void \1(\2) {', java_code)

    # Replace indentation (4 spaces -> tab)
    java_code = java_code.replace("    ", "    ")

    # Replace Python comments (#) with Java (//)
    java_code = re.sub(r'#(.*)', r'//\1', java_code)

    # Add class wrapper if missing
    java_code = "public class ConvertedCode {\n" + java_code + "\n}"

    return java_code


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_py_to_java.py <python_file>")
        sys.exit(1)

    py_file = Path(sys.argv[1])
    if not py_file.exists():
        print(f"Error: {py_file} not found")
        sys.exit(1)

    py_code = py_file.read_text()
    java_code = convert_python_to_java(py_code)

    java_file = py_file.with_suffix(".java")
    java_file.write_text(java_code)

    print(f"✅ Converted {py_file} -> {java_file}")


if __name__ == "__main__":
    main()
