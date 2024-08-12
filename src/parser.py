import ast

class CodeParser:
    def __init__(self, code):
        """
        Initialize the parser with the provided Python code.
        """
        self.tree = ast.parse(code)

    def get_functions(self):
        """
        Extract all functions from the code and return their names and docstrings.
        """
        functions = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                functions.append({
                    'name': node.name,
                    'doc': ast.get_docstring(node)
                })
        return functions

    def get_classes(self):
        """
        Extract all classes from the code and return their names, docstrings, and methods.
        """
        classes = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                cls = {
                    'name': node.name,
                    'doc': ast.get_docstring(node)
                }
                methods = []
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        methods.append({
                            'name': item.name,
                            'doc': ast.get_docstring(item)
                        })
                if methods:
                    cls['methods'] = methods
                classes.append(cls)
        return classes