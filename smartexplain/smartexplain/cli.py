import argparse
from smartexplain import explain_code
from rich.console import Console
import pyperclip
import json
import os

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Explain Python code like you're 5.")
    parser.add_argument('--file', help="Python file to explain")
    parser.add_argument('--code', help="Inline Python code string")
    parser.add_argument('--clip', action='store_true', help="Explain code from clipboard")
    parser.add_argument('--emoji-off', action='store_true', help="Disable emojis in output")
    parser.add_argument('--raw', action='store_true', help="Raw text output (no formatting)")
    parser.add_argument('--json', action='store_true', help="Output explanation as JSON")
    parser.add_argument('--output', type=str, help="Save the explanation to a file")

    args = parser.parse_args()

    if args.clip:
        code = pyperclip.paste()
    elif args.code:
        code = args.code
    elif args.file:
        if not os.path.exists(args.file):
            console.print(f"[red]❌ File '{args.file}' not found.[/red]")
            return
        with open(args.file, 'r', encoding='utf-8') as f:
            code = f.read()
    else:
        console.print("[yellow]⚠️ Please provide code with --file, --code or --clip[/yellow]")
        return

    explanation = explain_code(code, emoji=not args.emoji_off)

    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(explanation)
            console.print(f"[green]✅ Explanation saved to {args.output}[/green]")
        except Exception as e:
            console.print(f"[red]❌ Failed to save to {args.output}: {e}[/red]")
        return

    if args.raw:
        print(explanation)
    elif args.json:
        explanation_lines = explanation.strip().splitlines()
        print(json.dumps(explanation_lines, indent=2))
    else:
        console.print(explanation, style="bold cyan")

if __name__ == '__main__':
    main()
