import argparse
import toml
import re
import sys

# Регулярное выражение для проверки имени
VALID_NAME_REGEX = re.compile(r"^[a-z][a-z0-9_]*$")

# Парсер и проверка TOML
def parse_toml(file_path):
    try:
        with open(file_path, 'r') as f:
            return toml.load(f)
    except Exception as e:
        print(f"Error reading TOML file: {e}", file=sys.stderr)
        sys.exit(1)

# Проверка имени
def validate_name(name):
    if not VALID_NAME_REGEX.match(name):
        raise ValueError(f"Invalid name: {name}")

# Преобразование значения
def convert_value(value):
    if isinstance(value, int):
        return str(value)
    elif isinstance(value, list):
        return f"list({', '.join(map(convert_value, value))})"
    elif isinstance(value, str):
        return value
    elif isinstance(value, bool):
        return str(value).lower()  # Или "true"/"false" если нужен именно такой формат
    else:
        raise ValueError(f"Unsupported value type: {value}")


def evaluate_expression_in_string(string, context):
    def replace_expression(match):
        try:
            expression = match.group(1)
            for key in context:
                expression = expression.replace(key, str(context[key]))
            result = eval(expression)
            return str(result)
        except Exception as e:
            raise ValueError(f"Error evaluating expression '{expression}': {e}")
    return re.sub(r"\?\{(.*?)\}", replace_expression, string)


# Генерация выходного формата
def generate_config(data):
    output_lines = []
    context = {}

    for key, value in data.items():
        validate_name(key)
        if not isinstance(value, str) or not value.startswith("?{"):
            context[key] = value

    for key, value in data.items():
        if isinstance(value, str):
            value = evaluate_expression_in_string(value, context)

        output_lines.append(f"{key} = {convert_value(value)}")

    return "\n".join(output_lines)


# Основная функция
def main():
    parser = argparse.ArgumentParser(description="TOML to custom config converter")
    parser.add_argument("input_file", help="Path to the input TOML file")
    args = parser.parse_args()

    data = parse_toml(args.input_file)

    try:
        output = generate_config(data)
        print(output)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()