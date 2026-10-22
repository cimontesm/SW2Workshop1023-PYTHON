class Student:

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0.0
        total = 0
        for grade in self.grades:
            total += grade
        return total / len(self.grades)

    def check_honor(self):
        self.honor = self.calculate_average() >= 90

    def delete_grade(self, index):
        del self.grades[index]

    def report(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades count: {len(self.grades)}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Honor roll: {self.honor}")


def main():
    student = Student("x", "")
    student.add_grade(100)
    student.add_grade("Fifty")  # broken
    student.calculate_average()
    student.check_honor()
    student.delete_grade(5)  # IndexError
    student.report()


main()
