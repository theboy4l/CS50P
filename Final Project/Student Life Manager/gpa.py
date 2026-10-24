class GPA:
    def __init__(self, subject, grade):
        self.subject = subject
        self.gradder = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0, "O": 0, "U": 0}
        self.grade = grade

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        self._subject = subject

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if grade not in self.gradder:
            raise ValueError("Invalid grade")
        self._grade = grade


class GPA_Manager:
    def __init__(self):
        self.subjects = []

    def add_subjects(self, subject, grade):
        subjects = GPA(subject, grade)
        self.subjects.append(subjects)

    def calculate_gpa(self):
        if not self.subjects:
            return None
        total = 0
        for subject in self.subjects:
            total += subject.gradder[subject.grade]
        gpa = float(total / len(self.subjects))
        return f"{gpa:.2f}"


def gpa_menu():
    gpa_manager = GPA_Manager()
    while True:
        print("""
        ===========Calculate GPA=================
                                                |
        1. Add Subjects and Grade               |
        2. Calculate GPA                        |
        3. Back                                 |
                                                |
        =========================================
        """)
        choice = input("Choice: ")
        match choice:
            case "1":
                subject = input("Enter Subject: ").strip()
                grade = input("Enter Grade: ").strip()
                gpa_manager.add_subjects(subject, grade)
            case "2":
                if not gpa_manager.subjects:
                    print("Please add subjects and grades first (Option 1).")
                else:
                    print(f"Your GPA is: {gpa_manager.calculate_gpa()}")
            case "3":
                break
