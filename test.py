class Student:

    def __init__(self, student_id, name):
        self.student_id = self._validate_text(student_id, "Student ID")
        self.name = self._validate_text(name, "Name")
        self.grades = []
        self.is_passed = False
        self.honor = False

    @staticmethod
    def _validate_text(value, field_name):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty string.")
        return value.strip()

    @staticmethod
    def _validate_grade(grade):
        is_number = isinstance(grade, (int, float))
        if not is_number or isinstance(grade, bool):
            raise ValueError(f"Grade must be numeric, got {grade!r}.")
        if not 0 <= grade <= 100:
            raise ValueError(f"Grade must be between 0 and 100, got {grade}.")
        return float(grade)

    def add_grade(self, grade):
        self.grades.append(self._validate_grade(grade))

    def calculate_average(self):
        if not self.grades:
            return 0.0
        total = 0
        for grade in self.grades:
            total += grade
        return total / len(self.grades)

    def letter_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    def check_passed(self):
        self.is_passed = self.calculate_average() >= 60

    def check_honor(self):
        self.honor = self.calculate_average() >= 90

    def delete_grade(self, index):
        del self.grades[index]

    def report(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades count: {len(self.grades)}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Letter grade: {self.letter_grade()}")
        print(f"Status: {'Passed' if self.is_passed else 'Failed'}")
        print(f"Honor roll: {self.honor}")


def main():
    student = Student("x", "")
    student.add_grade(100)
    student.add_grade("Fifty")  # broken
    student.calculate_average()
    student.check_passed()
    student.check_honor()
    student.delete_grade(5)  # IndexError
    student.report()


main()
