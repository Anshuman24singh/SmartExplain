import unittest
from smartexplain.explainer import explain_code

class TestExplainCode(unittest.TestCase):

    def test_function_definition(self):
        code = "def say_hello():\n    return 'hello'"
        explanation = explain_code(code)
        self.assertIn("🧩 This defines a function named `say_hello`.", explanation)

    def test_print_statement(self):
        code = "print('Hello')"
        explanation = explain_code(code)
        self.assertIn("🖨️ This line prints something to the screen.", explanation)

    def test_for_loop(self):
        code = "for i in range(5):\n    print(i)"
        explanation = explain_code(code)
        self.assertIn("🔁 This is a for loop that repeats a block of code.", explanation)

    def test_if_statement(self):
        code = "if x > 5:\n    print('Big')"
        explanation = explain_code(code)
        self.assertIn("❓ This is an if statement that checks a condition", explanation)

    def test_invalid_code(self):
        code = "def broken("
        explanation = explain_code(code)
        self.assertIn("⚠️ Invalid Python syntax.", explanation)

    def test_no_explanation(self):
        code = "pass"
        explanation = explain_code(code)
        self.assertIn("🤔 Couldn’t find anything explainable", explanation)

if __name__ == '__main__':
    unittest.main()
