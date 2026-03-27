expenses = []

print("=== Expense Tracker ===")

while True:
    amount = input("Enter amount (or type 'q' to quit): ")

    if amount.lower() == 'q':
        break

    if amount == "":
        print("Amount cannot be empty.")
        continue

    try:
        amount = float(amount)
        if amount < 0:
            print("Amount cannot be negative.")
            continue
    except ValueError:
        print("Invalid amount. Try again.")
        continue

    category = input("Enter category: ")

    if category == "":
        category = "uncategorized"

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added!\n")


total = sum(exp["amount"] for exp in expenses)

print("\n=== Summary ===")
print(f"Total expenses: {total:.2f}")

print("\nAll Expenses:")
for exp in expenses:
    print(f"{exp['category']}: {exp['amount']}")