import datetime


class Study:
    def __init__(self, subject, study_time_goal, start_time, end_time):
        self.completed_topics = []
        self.subject = subject
        self.start_time = start_time
        self.end_time = end_time
        self.study_time_goal = study_time_goal
        self.elapsed_time = None

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        if not isinstance(subject, str) or not subject.strip() or subject.isdigit():
            raise ValueError("Subject must be a non-empty string.")
        self._subject = subject

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
    def study_time_goal(self):
        return self._study_time_goal

    @study_time_goal.setter
    def study_time_goal(self, minutes):
        if not isinstance(minutes, int) or minutes <= 0:
            raise ValueError("Please enter a proper number of minutes.")
        self._study_time_goal = minutes

    def calculate_elapsed(self):
        today = datetime.date.today()
        start = datetime.datetime.combine(today, self.start_time)
        end = datetime.datetime.combine(today, self.end_time)
        elapsed = end - start
        self.elapsed_time = elapsed.total_seconds() / 3600
        return self.elapsed_time

    def complete_topic(self, topic):
        try:
            if not isinstance(topic, str) or not topic.strip() or topic.isdigit():
                raise ValueError
            self.completed_topics.append(topic.strip().capitalize())
            print(f"Topic '{topic.capitalize()}' added successfully!")
        except ValueError:
            print("Enter the expected value (a valid text topic).")

    def __str__(self):
        elapsed = self.elapsed_time if self.elapsed_time is not None else self.calculate_elapsed()
        return (
            f"{self.subject} | "
            f"Goal: {self.study_time_goal} mins | "
            f"Elapsed: {elapsed:.2f} hrs | "
            f"Topics: {self.completed_topics}"
        )


def get_time(prompt):
    while True:
        try:
            hour, minute = input(prompt).split(":")
            return datetime.time(int(hour), int(minute))
        except ValueError:
            print("Use this format: HH:MM (example: 08:30)")


def Study_menu():
    subject = input("Subject: ")
    goal_t = int(input("Study goal (in minutes): "))
    start_t = get_time("Start time (HH:MM): ")
    end_t = get_time("End time (HH:MM): ")
    session = Study(subject, goal_t, start_t, end_t)

    while True:
        print("""
1. View session / Update Goal
2. Calculate elapsed time
3. Add completed topic
4. Back
""")
        choice = input("What do you want to do? ")
        match choice:
            case "1":
                print(session)
                update = input("Update goal? (y/n): ")
                if update.lower() == "y":
                    session.study_time_goal = int(input("New study goal (in minutes): "))
            case "2":
                print(f"Elapsed time: {session.calculate_elapsed():.2f} hours")
            case "3":
                topic = input("Topic: ")
                session.complete_topic(topic)
            case "4":
                print("Going back...")
                break
            case _:
                print("Choose one of the options above.")
