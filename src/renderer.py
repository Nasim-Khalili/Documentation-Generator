class DocumentationRenderer:
    def __init__(self, functions, classes):
        """
        Initialize the renderer with functions and classes extracted from the code.
        """
        self.functions = functions
        self.classes = classes

    def render_markdown(self):
        """
        Generate Markdown documentation for the functions and classes.
        """
        markdown = "# Documentation\n\n"

        # Classes
        if self.classes:
            markdown += "## Classes\n"
            for cls in self.classes:
                cls_name = cls.get('name', 'Unknown Class')
                cls_doc = cls.get('doc', 'No documentation available')
                markdown += f"### {cls_name}\n{cls_doc}\n\n"
                if 'methods' in cls:
                    markdown += "#### Methods:\n"
                    for method in cls['methods']:
                        method_name = method.get('name', 'Unknown Method')
                        method_doc = method.get('doc', 'No documentation available')
                        markdown += f"- **{method_name}**: {method_doc}\n"
                    markdown += "\n"

        # Functions
        if self.functions:
            markdown += "## Functions\n"
            for func in self.functions:
                func_name = func.get('name', 'Unknown Function')
                func_doc = func.get('doc', 'No documentation available')
                markdown += f"### {func_name}\n{func_doc}\n\n"

        return markdown