"""A one-transaction ATM simulator for the Week 2 project."""


balance = 100.00

print("ATM Simulator")
print("1. Check balance")
print("2. Deposit")
print("3. Withdraw")
choice = input("Choose an option (1-3): ").strip()

if choice == "1":
    print(f"Current balance: ${balance:.2f}")
elif choice == "2":
    amount = float(input("Deposit amount: "))
    if amount <= 0:
        print("Enter an amount greater than zero. Balance unchanged.")
    else:
        balance = balance + amount
        print(f"Deposit approved. New balance: ${balance:.2f}")
elif choice == "3":
    amount = float(input("Withdrawal amount: "))
    if amount <= 0:
        print("Enter an amount greater than zero. Balance unchanged.")
    elif amount > balance:
        print("Insufficient funds. Balance unchanged.")
    else:
        balance = balance - amount
        print(f"Withdrawal approved. New balance: ${balance:.2f}")
else:
    print("Unknown option. Choose 1, 2, or 3.")
