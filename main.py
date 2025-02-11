from expense import Expense
from expense_tracker import ExpenseTracker

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n=== Expense Tracker Menu ===")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. View Total Expenses")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            date = input("Enter expense date (YYYY-MM-DD): ")
            description = input("Enter expense description: ")
            try:
                amount = float(input("Enter expense amount: "))
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                continue
            expense = Expense(date, description, amount)
            tracker.add_expense(expense)
            print("Expense added successfully.")

        elif choice == '2':
            if not tracker.expenses:
                print("No expenses to remove.")
                continue
            tracker.view_expenses()
            try:
                index = int(input("Enter the expense number to remove: "))
                tracker.remove_expense(index - 1)  # Adjust for 0-indexed list
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '3':
            tracker.view_expenses()

        elif choice == '4':
            tracker.total_expenses()

        elif choice == '5':
            print("Exiting the expense tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select an option from the menu.")

if __name__ == "__main__":
    main()
