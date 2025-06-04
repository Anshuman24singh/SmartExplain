import sys
from smartexplain import explain_code

def main():
    if len(sys.argv) != 2:
        print("Usage: smartexplain <your_file.py>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
            explanation = explain_code(code)
            print(explanation)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error: {e}")
