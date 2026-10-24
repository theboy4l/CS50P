from datetime import date


class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        try:
            if not description or description == "" or isinstance(description, int):
                raise ValueError
            self._description = description
        except ValueError:
            print("Enter a valid description")
            raise

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        try:
            if priority not in [1, 2, 3]:
                raise ValueError
            self._priority = priority
        except ValueError:
            print("Enter a valid priority")
            raise

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        try:
            if not isinstance(due_date, date):
                raise TypeError
            self._due_date = due_date
        except (TypeError, ValueError):
            print("Enter a valid date")
            raise

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, completed):
        try:
            if not isinstance(completed, bool):
                raise ValueError
            self._completed = completed
        except ValueError:
            print("Incorrect value")
            raise

    def __str__(self):
        return (
            f"\nDescription : {self.description}\n"
            f"Due Date : {self.due_date}\n"
            f"Priority : {self.priority}\n"
            f"Completed : {self.completed}\n"
        )


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def complete_task(self):
        try:
            index = int(input("Task number: "))
            task = self.tasks[index - 1]
            task.completed = True
            print(f"Task {index} marked as completed.")
        except (IndexError, ValueError):
            print("Invalid task number.")

    def sort_by_priority(self):
        sorted_list = sorted(self.tasks, key=lambda task: task.priority)
        for i, task in enumerate(sorted_list, 1):
            print(f"{i}: {task}")

    def sort_by_due_date(self):
        sorted_list = sorted(self.tasks, key=lambda task: task.due_date)
        for task in sorted_list:
            print(task)

    def remove_task(self, index):
        try:
            index = int(index)
            self.tasks.pop(index - 1)
            print(f"Task {index} removed successfully.")
        except (IndexError, ValueError):
            print("Invalid option.")


def get_date(user_date):
    try:
        year, month, day = user_date.strip().split("-")
        return date(int(year), int(month), int(day))
    except ValueError:
        print("Invalid date")


def tasks_menu():
    task_manager = TaskManager()
    while True:
        print("""==========TASK MANAGER=========
1. Add task
2. List Tasks
3. Complete Tasks
4. Sort by due date
5. Back
================================""")
        choice = input("Choice: ")
        match choice:
            case "1":
                description = input("Description: ")
                d_date = input("Due date: ")
                due_date = get_date(d_date)
                priority = int(input("Priority: "))
                task_manager.add_task(description, due_date, priority)
            case "2":
                task_manager.list_tasks()
            case "3":
                task_manager.complete_task()
            case "4":
                task_manager.sort_by_due_date()
            case "5":
                break
