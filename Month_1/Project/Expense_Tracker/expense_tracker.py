"""An in-memory command-line expense tracker."""


def add_expense(expenses, description, amount):
    description = description.strip()
    if not description:
        raise ValueError("Description cannot be blank.")
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    expense = {"description": description, "amount": amount}
    expenses.append(expense)
    return expense


def calculate_total(expenses):
    total = 0.0
    for expense in expenses:
        total = total + expense["amount"]
    return total


def read_amount():
    amount_text = input("Amount: ")
    try:
        amount = float(amount_text)
    except ValueError:
        print("Enter a numeric amount, such as 12.50.")
        return None

    if amount <= 0:
        print("Amount must be greater than zero.")
        return None
    return amount


def add_expense_from_input(expenses):
    description = input("Description: ")
    amount = read_amount()
    if amount is None:
        return

    try:
        add_expense(expenses, description, amount)
    except ValueError as error:
        print(error)
        return
    print("Expense added.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']}: ${expense['amount']:.2f}")


def main():
    expenses = []
    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View total")
        print("4. Quit")
        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                add_expense_from_input(expenses)
            case "2":
                show_expenses(expenses)
            case "3":
                print(f"Total: ${calculate_total(expenses):.2f}")
            case "4":
                print("Goodbye.")
                break
            case _:
                print("Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
