import csv
import os
from expense import Expense

class ExpenseTracker:
    def __init__(self, filename = "expenses.csv"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            self.save_expenses()
            print("Expense removed successfully.")
        else:
            print("Invalid expense index.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. {expense}")  # Uses Expense.__str__()

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")


    def save_expenses(self):
        """
        Save the list of expenses to a CSV file.
        """
        try:
            with open(self.filename, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                # Write header row
                writer.writerow(["date", "description", "amount"])
                # Write each expense row
                for expense in self.expenses:
                    writer.writerow(expense.to_csv_row())
        except Exception as e:
            print("Error saving expenses to CSV:", e)

    def load_expenses(self):
        """
        Load the list of expenses from a CSV file, if it exists.
        """
        if os.path.exists(self.filename):
            try:
                with open(self.filename, mode='r', newline='', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile)
                    # Skip header row
                    next(reader, None)
                    self.expenses = [Expense.from_csv_row(row) for row in reader if row]
            except Exception as e:
                print("Error loading expenses from CSV:", e)
                self.expenses = []
