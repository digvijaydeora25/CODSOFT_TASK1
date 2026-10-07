
def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    elif operator == "**":
        return num1 ** num2
    elif operator == "%":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 % num2
    else:
        return "Error: Invalid operator."


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("===== SIMPLE CALCULATOR =====")
    print("Supported operators: + - * / ** %")

    while True:
        num1 = get_number("Enter first number: ")
        operator = input("Enter operator (+, -, *, /, **, %): ").strip()
        num2 = get_number("Enter second number: ")

        result = calculate(num1, operator, num2)
        print(f"Result: {result}")

        again = input("\nDo another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()