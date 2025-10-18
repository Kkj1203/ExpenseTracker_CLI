import json
from datetime import datetime

FILE_NAME = "expenses.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(date, category, amount):
    expenses = load_data()
    expenses.append({"date": date, "category": category, "amount": amount})
    save_data(expenses)
    print("✅ Expense added successfully!")

def view_summary():
    expenses = load_data()
    if not expenses:
        print("No expenses yet.")
        return

    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    print("\n📊 Expense Summary:")
    for category, total in summary.items():
        print(f"{category}: ₹{total}")

def main():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ") or datetime.today().strftime("%Y-%m-%d")
            category = input("Enter category (Food, Travel, etc.): ")
            amount = float(input("Enter amount: "))
            add_expense(date, category, amount)

        elif choice == "2":
            view_summary()

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
