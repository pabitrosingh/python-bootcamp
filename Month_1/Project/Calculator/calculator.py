"""A four-operation command-line calculator."""


def calculate(first_number, operation, second_number):
    if operation == "+":
        return first_number + second_number
    if operation == "-":
        return first_number - second_number
    if operation == "*":
        return first_number * second_number
    if operation == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
    raise ValueError("Choose one of: +, -, *, /.")


def main():
    first_number = float(input("First number: "))
    operation = input("Operation (+, -, *, /): ").strip()
    second_number = float(input("Second number: "))

    try:
        result = calculate(first_number, operation, second_number)
    except (ValueError, ZeroDivisionError) as error:
        print(error)
        return

    print(f"Result: {result:.2f}")


if __name__ == "__main__":
    main()
