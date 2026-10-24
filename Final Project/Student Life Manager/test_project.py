from timetable import TimetableManager
from gpa import GPA_Manager
from budget import ManageExpense
from tasks import TaskManager
from study import Study
from budget import Budget
import datetime
import pytest

from project import validate_menu_choice, display_menu, handle_menu_choice


def test_validate_menu_choice_valid():
    assert validate_menu_choice("1") == 1


def test_validate_menu_choice_invalid():
    assert validate_menu_choice("hello") is None
    assert validate_menu_choice("99") is None


def test_handle_menu_choice_exit():
    assert handle_menu_choice(6) is False


def test_adding():
    manager = TaskManager()
    manager.add_task(description="Finish assignment", due_date=datetime.date(2026, 5, 20), priority=1)
    assert len(manager.tasks) == 1


def test_remove_task():
    manager = TaskManager()
    manager.add_task(description="Buy groceries", due_date=datetime.date(2026, 5, 21), priority=2)
    manager.remove_task(1)
    assert len(manager.tasks) == 0


def test_invalid_priority_raises_error():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task(description="Invalid Task", due_date=datetime.date(2026, 5, 22), priority=5)


def test_add_entry():
    manager = TimetableManager()
    start = datetime.time(9, 0)
    end = datetime.time(10, 30)
    manager.add_entry(day="Monday", start_time=start, end_time=end, subject="Math")
    assert len(manager.entries) == 1


def test_remove_entry():
    manager = TimetableManager()
    start = datetime.time(9, 0)
    end = datetime.time(10, 0)
    manager.add_entry(day="Tuesday", start_time=start, end_time=end, subject="Physics")
    manager.remove_entry(1)
    assert len(manager.entries) == 0


def test_add_expense():
    manager = ManageExpense()
    manager.add_expense(description="Groceries", category="Food", price=45.50)
    assert len(manager.expenses) == 1


def test_remove_expense():
    manager = ManageExpense()
    manager.add_expense(description="Bus ticket", category="Transportation", price=2.50)
    manager.remove_expense(1)
    assert len(manager.expenses) == 0


def test_invalid_price_raises_error():
    manager = ManageExpense()
    with pytest.raises(ValueError):
        manager.add_expense(description="Rent", category="Housing", price=-500)


# Testing the study class
