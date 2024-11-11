import datetime

class Expense:
    def __init__(self, description, amount, date=None):
        self.description = description
        self.amount = amount
        self.date = date if date else datetime.date.today()
        
    def __str__(self):
        return f"{self.date} - {self.description}: ${self.amount:.2f}"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        expense = Expense(description, amount)
        self.expenses.append(expense)
        print("Expense added.")

    def update_expense(self, index, description, amount):
        if 0 <= index < len(self.expenses):
            self.expenses[index].description = description
            self.expenses[index].amount = amount
            print("Expense updated.")
        else:
            print("Invalid expense index.")

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense deleted.")
        else:
            print("Invalid expense index.")

    def view_expenses(self):
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense}")

    def summary(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")

    def monthly_summary(self, month, year):
        monthly_expenses = [expense for expense in self.expenses if expense.date.month == month and expense.date.year == year]
        total = sum(expense.amount for expense in monthly_expenses)
        print(f"Total Expenses for {month}/{year}: ${total:.2f}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Update Expense")
        print("3. Delete Expense")
        print("4. View Expenses")
        print("5. Summary of All Expenses")
        print("6. Monthly Summary")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(description, amount)
        elif choice == '2':
            index = int(input("Enter expense index to update: ")) - 1
            description = input("Enter new description: ")
            amount = float(input("Enter new amount: "))
            tracker.update_expense(index, description, amount)
        elif choice == '3':
            index = int(input("Enter expense index to delete: ")) - 1
            tracker.delete_expense(index)
        elif choice == '4':
            tracker.view_expenses()
        elif choice == '5':
            tracker.summary()
        elif choice == '6':
            month = int(input("Enter month (MM): "))
            year = int(input("Enter year (YYYY): "))
            tracker.monthly_summary(month, year)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
