def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average


def main():
    try:
        grades = []
        for i in range(3):
            grade = float(input(f"Enter the grade for subject {i + 1}: "))
            grades.append(grade)

        average = calculate_average(grades)
        print(f"The average grade is: {average:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numeric grades.")


if __name__ == "__main__":
    main()
