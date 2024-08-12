import unittest
from src.parser import CodeParser

class TestCodeParser(unittest.TestCase):
    def test_get_functions(self):
        code = "def foo(): pass"
        parser = CodeParser(code)
        functions = parser.get_functions()
        self.assertEqual(functions[0]['name'], "foo")

    def test_get_classes(self):
        code = "class Foo: pass"
        parser = CodeParser(code)
        classes = parser.get_classes()
        self.assertEqual(classes[0]['name'], "Foo")

if __name__ == "__main__":
    unittest.main()