# Student Life Manager

Student Life Manager is a Python command-line application designed to help students manage academic and personal tasks in one place. It brings together task management, timetables, budgeting, study sessions, and GPA calculations.

The project uses Python, object-oriented programming, classes, properties, exception handling, lists, datetime, match/case, and pytest.

## Features

### Task Manager
Create tasks with a description, due date, priority, and completion status. View, complete, sort, and remove tasks.

### Timetable Manager
Add timetable entries with a day, start time, end time, and subject. View, edit, and remove entries.

### Budget Manager
Track expenses with a description, category, price, and date. Add, view, and remove expenses.

### Study Session Manager
Create study sessions with a subject, study-time goal, start time, and end time. Calculate elapsed time and record completed topics.

### GPA Calculator
Enter subjects and grades and calculate a GPA using the grading scale implemented in the application.

## Files

- project.py — Main menu and navigation.
- tasks.py — Task and TaskManager classes.
- timetable.py — TimetableEntry and TimetableManager classes.
- budget.py — Budget and ManageExpense classes.
- study.py — Study session class and menu.
- gpa.py — GPA classes and calculator menu.
- test_project.py — Automated tests written with pytest.
- requirements.txt — External packages required by this project.

## Run

Install the project dependencies with:

    python -m pip install -r requirements.txt

Start the application with:

    python project.py

Run the tests with:

    pytest
