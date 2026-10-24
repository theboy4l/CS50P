from timetable import TimetableManager, timetable_menu
from gpa import GPA_Manager, gpa_menu
from budget import ManageExpense, budget_menu
from study import Study_menu
from tasks import tasks_menu

timetable_manager = TimetableManager()
gpa_manager = GPA_Manager()
expense_manager = ManageExpense()


def main():
    while True:
        display_menu()
        raw_choice = input("Enter your choice: ")
        choice = validate_menu_choice(raw_choice)
        if not handle_menu_choice(choice):
            break


def display_menu():
    """Print the main menu interface."""
    print(
        """
 ===========Student Manager============

 1. Tasks
 2. Timetable
 3. Budget
 4. Study Sessions
 5. GPA Calculator
 6. Exit

 ====================================
 """
    )


def validate_menu_choice(choice):
    """Validate user input and return an integer choice if valid."""
    try:
        choice = int(choice)
        if choice in [1, 2, 3, 4, 5, 6]:
            return choice
        return None
    except ValueError:
        return None


def handle_menu_choice(choice):
    match choice:
        case 1:
            tasks_menu()
        case 2:
            timetable_menu()
        case 3:
            budget_menu()
        case 4:
            Study_menu()
        case 5:
            gpa_menu()
        case 6:
            print("Exiting Student Manager. Goodbye!")
            return False
        case _:
            print("Invalid Choice. Please enter a number between 1 and 6.")
    return True


if __name__ == "__main__":
    main()
