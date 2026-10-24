import datetime


class Budget:
    def __init__(self, description, category, price):
        self.description = description
        self.category = category
        self.price = price
        self.date = datetime.date.today()

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if not description:
            raise ValueError("Description cannot be empty")
        self._description = description

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        categories = ["Housing", "Utilities", "Food", "Transportation", "Healthcare", "Debt & Family"]
        if category not in categories:
            raise ValueError("Invalid category")
        self._category = category

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price = price

    def __str__(self):
        return f"{self.description} | {self.category} | $" + str(self.price) + f" | {self.date}"


class ManageExpense:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, category, price):
        expense = Budget(description, category, price)
        self.expenses.append(expense)

    def list_expenses(self):
        if not self.expenses:
            print("No expenses available")
            return
        for index, expense in enumerate(self.expenses, 1):
            print(f"{index}. {expense}")

    def remove_expense(self, index):
        if not self.expenses:
            print("No expenses available")
            return
        try:
            self.list_expenses()
            index = int(index) - 1
            removed = self.expenses.pop(index)
            print(f"Removed: {removed.description}")
        except ValueError:
            print("Please enter a valid number")
        except IndexError:
            print("Invalid option")


def budget_menu():
    manager = ManageExpense()
    while True:
        print("""
======== Expense Manager ========

1. Add Expense
2. View Expenses
3. Remove Expense
4. Exit

=================================
""")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                try:
                    description = input("Description: ")
                    category = input("Category (Housing, Utilities, Food, Transportation, Healthcare, Debt & Family): ")
                    price = float(input("Price: "))
                    manager.add_expense(description, category, price)
                    print("Expense added successfully")
                except ValueError:
                    print("Error")
            case "2":
                manager.list_expenses()
            case "3":
                index = input("Enter expense number to remove: ")
                manager.remove_expense(index)
            case "4":
                print("Goodbye!")
                break
            case _:
                print("Invalid option")
