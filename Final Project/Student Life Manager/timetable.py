import datetime
from tabulate import tabulate


class TimetableEntry:
    def __init__(self, day, start_time, end_time, subject):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.subject = subject

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        if day not in valid_days:
            print("Hmm that doesn't look like a valid day.")
            raise ValueError("Invalid day")
        self._day = day

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        if not isinstance(start_time, datetime.time):
            print("That doesn't look like a proper time.")
            raise TypeError("start_time must be datetime.time")
        self._start_time = start_time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        if not isinstance(end_time, datetime.time):
            print("Please enter a proper time.")
            raise TypeError("end_time must be datetime.time")
        if end_time <= self.start_time:
            print("The end time has to come after the start time.")
            raise ValueError("End time must be after start time")
        self._end_time = end_time

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        if not subject or not isinstance(subject, str) or subject.strip() == "":
            print("A subject name can't be empty.")
            raise ValueError("Invalid subject")
        self._subject = subject

    def __str__(self):
        return (
            f"{self.day} | "
            f"{self.start_time.strftime('%H:%M')} - "
            f"{self.end_time.strftime('%H:%M')} | "
            f"{self.subject}"
        )


class TimetableManager:
    def __init__(self):
        self.entries = []

    def add_entry(self, day, start_time, end_time, subject):
        entry = TimetableEntry(day, start_time, end_time, subject)
        self.entries.append(entry)
        print("Added to your timetable.")

    def view_timetable(self):
        if not self.entries:
            print("Nothing on your timetable yet.")
            return

        table = []
        for number, entry in enumerate(self.entries, start=1):
            table.append([
                number,
                entry.day,
                entry.start_time.strftime("%H:%M"),
                entry.end_time.strftime("%H:%M"),
                entry.subject
            ])

        print(tabulate(
            table,
            headers=["No.", "Day", "Start", "End", "Subject"],
            tablefmt="grid"
        ))

    def remove_entry(self, index):
        try:
            index = int(index) - 1
            removed_entry = self.entries.pop(index)
            print(f"Removed {removed_entry.subject} from your timetable.")
        except IndexError:
            print("That entry number doesn't exist.")
        except ValueError:
            print("Please enter a number.")

    def edit_entry(self):
        if not self.entries:
            print("Nothing to edit yet.")
            return

        self.view_timetable()
        try:
            index = int(input("Which entry do you want to edit? ")) - 1
            entry = self.entries[index]
            choice = int(input("""
What would you like to change?

1. Day
2. Start time
3. End time
4. Subject

Choice:
"""))
            if choice == 1:
                entry.day = input("New day: ")
            elif choice == 2:
                entry.start_time = get_time()
            elif choice == 3:
                entry.end_time = get_time()
            elif choice == 4:
                entry.subject = input("New subject: ")
            else:
                print("That option isn't available.")
                return
            print("Timetable updated.")
        except IndexError:
            print("That entry doesn't exist.")
        except ValueError:
            print("Please enter a valid number.")


def get_time():
    while True:
        user_time = input("Enter time (HH:MM): ")
        try:
            hour, minute = user_time.split(":")
            return datetime.time(int(hour), int(minute))
        except ValueError:
            print("Use this format: HH:MM (example: 08:30)")


def timetable_menu():
    timetable_manager = TimetableManager()
    while True:
        print("""
1. Add timetable entry
2. View timetable
3. Edit entry
4. Remove entry
5. Back
""")
        choice = input("What do you want to do? ")
        match choice:
            case "1":
                day = input("Day: ")
                start = get_time()
                end = get_time()
                subject = input("Subject: ")
                timetable_manager.add_entry(day, start, end, subject)
            case "2":
                timetable_manager.view_timetable()
            case "3":
                timetable_manager.edit_entry()
            case "4":
                index = input("Entry number to remove: ")
                timetable_manager.remove_entry(index)
            case "5":
                print("Going back...")
                break
            case _:
                print("Choose one of the options above.")
