def calculate_final_value(initial_capital, interest_rate, investment_time):
    final_value = initial_capital * (1 + (interest_rate / 100)) ** investment_time
    return final_value


def main():
    try:
        initial_capital = float(input("Enter the initial capital: "))
        interest_rate = float(input("Enter the interest rate (annual percentage): "))
        investment_time = int(input("Enter the investment time (in months): "))

        final_value = calculate_final_value(initial_capital, interest_rate, investment_time)
        print(f"The final value of the investment is: {final_value:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")


if __name__ == "__main__":
    main()
