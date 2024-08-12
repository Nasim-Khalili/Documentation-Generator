import argparse
from .parser import CodeParser
from .renderer import DocumentationRenderer

def main():
    """
    Main function that parses command line arguments, generates documentation,
    and writes it to a Markdown file.
    """
    parser = argparse.ArgumentParser(description="Generate documentation from Python code.")
    parser.add_argument("filepath", help="Path to the Python file")
    args = parser.parse_args()

    with open(args.filepath, "r") as file:
        code = file.read()

    code_parser = CodeParser(code)
    functions = code_parser.get_functions()
    classes = code_parser.get_classes()

    renderer = DocumentationRenderer(functions, classes)
    markdown = renderer.render_markdown()

    with open("DOCUMENTATION.md", "w") as doc_file:
        doc_file.write(markdown)
    print("Documentation generated and saved to DOCUMENTATION.md")

if __name__ == "__main__":
    main()