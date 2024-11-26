import unittest
from converter import convert_value, validate_name, generate_config, evaluate_expression_in_string

class TestConfigConverter(unittest.TestCase):
    def test_convert_value(self):
        self.assertEqual(convert_value(42), "42")
        self.assertEqual(convert_value([1, 2, 3]), "list(1, 2, 3)")
        self.assertEqual(convert_value("hello"), "hello")
        self.assertEqual(convert_value(True), "True")  # Обратите внимание на строчное "true"
        self.assertEqual(convert_value(False), "False")

    def test_validate_name(self):
        validate_name("valid_name")
        with self.assertRaises(ValueError):
            validate_name("Invalid-Name")

    def test_generate_config(self):
        data = {"key": 123, "list_key": [1, 2, 3], "string_key": "hello", "bool_key": True}
        output = generate_config(data)
        self.assertEqual(output, "key = 123\nlist_key = list(1, 2, 3)\nstring_key = hello\nbool_key = True")

    def test_evaluate_expression(self):
      context = {"x": 10, "y": 5}
      self.assertEqual(evaluate_expression_in_string("?{x + y}", context), "15")
      self.assertEqual(evaluate_expression_in_string("?{x * 2}", context), "20")
      with self.assertRaises(ValueError):
          evaluate_expression_in_string("?{x + z}", context)
    
    def test_generate_config_with_expressions(self):
        data = {"base_value": 10, "calculated_value": "?{base_value * 2}", "message": "Result: ?{base_value * 2}"}
        output = generate_config(data)
        self.assertEqual(output, "base_value = 10\ncalculated_value = 20\nmessage = Result: 20")


if __name__ == "__main__":
    unittest.main()