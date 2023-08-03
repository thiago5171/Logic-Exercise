def factorial(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result


def main():
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(num)
            print(f"The factorial of {num} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")


if __name__ == "__main__":
    main()
