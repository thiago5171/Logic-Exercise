def simple_calculator(num1, num2, operator):
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error: Cannot divide by zero",
    }

    if operator in operators:
        return operators[operator](num1, num2)
    else:
        raise ValueError("Invalid operator")


def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /): ")

        if operator not in ['+', '-', '*', '/']:
            raise ValueError("Invalid operator")

        result = simple_calculator(num1, num2, operator)
        print(f"The result of the operation is: {result}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")


if __name__ == "__main__":
    main()
