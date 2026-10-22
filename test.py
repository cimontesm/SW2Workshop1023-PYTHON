"""
Refactored version of the base code following PEP 8 and meeting
the requirements.
"""

MIN_GRADE = 0.0
MAX_GRADE = 100.0
PASSING_AVERAGE = 60.0
HONOR_ROLL_AVERAGE = 90.0

LETTER_THRESHOLDS = (
    (90.0, "A"),
    (80.0, "B"),
    (70.0, "C"),
    (60.0, "D"),
)


class Student:
    """A student with an ID, a name and a list of numeric grades."""

    def __init__(self, student_id, name):
        """Create a student, validating that ID and name are not empty."""
        self.student_id = self._validate_text(student_id, "Student ID")
        self.name = self._validate_text(name, "Name")
        self.grades = []

    @staticmethod
    def _validate_text(value, field_name):
        """Return the stripped text, or raise ValueError if it is empty."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty string.")
        return value.strip()

    @staticmethod
    def _validate_grade(grade):
        """Return the grade as a float, or raise ValueError if invalid."""
        is_number = isinstance(grade, (int, float))
        if not is_number or isinstance(grade, bool):
            raise ValueError(f"Grade must be numeric, got {grade!r}.")
        if not MIN_GRADE <= grade <= MAX_GRADE:
            raise ValueError(
                f"Grade must be between {MIN_GRADE:g} and {MAX_GRADE:g}, "
                f"got {grade}."
            )
        return float(grade)

    def add_grade(self, grade):
        """Add a validated grade to the student's record."""
        self.grades.append(self._validate_grade(grade))

    def calculate_average(self):
        """Return the average grade, or 0.0 if there are no grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def letter_grade(self):
        """Return the letter grade for the current average."""
        average = self.calculate_average()
        for threshold, letter in LETTER_THRESHOLDS:
            if average >= threshold:
                return letter
        return "F"

    def has_passed(self):
        """Return True if the average is at or above the passing mark."""
        return self.calculate_average() >= PASSING_AVERAGE

    def is_on_honor_roll(self):
        """Return True if the average qualifies for the honor roll."""
        return self.calculate_average() >= HONOR_ROLL_AVERAGE

    def remove_grade_by_index(self, index):
        """Remove and return the grade at the given position."""
        if not isinstance(index, int) or isinstance(index, bool):
            raise ValueError(f"Index must be an integer, got {index!r}.")
        if not 0 <= index < len(self.grades):
            raise IndexError(
                f"Index {index} is out of range; "
                f"student has {len(self.grades)} grade(s)."
            )
        return self.grades.pop(index)

    def remove_grade_by_value(self, value):
        """Remove the first occurrence of a grade value."""
        grade = self._validate_grade(value)
        if grade not in self.grades:
            raise ValueError(f"Grade {grade} was not found.")
        self.grades.remove(grade)
        return grade

    def summary_report(self):
        """Return a formatted summary of the student's record."""
        status = "Passed" if self.has_passed() else "Failed"
        honor = "Yes" if self.is_on_honor_roll() else "No"
        lines = [
            "----- Student Summary -----",
            f"ID:            {self.student_id}",
            f"Name:          {self.name}",
            f"Grades count:  {len(self.grades)}",
            f"Average:       {self.calculate_average():.2f}",
            f"Letter grade:  {self.letter_grade()}",
            f"Status:        {status}",
            f"Honor roll:    {honor}",
        ]
        return "\n".join(lines)


def main():
    """Demonstrate the opertional state of the system."""
    student = Student("x", "")
    student.add_grade(100)
    student.add_grade("Fifty")  # broken
    student.remove_grade_by_index(5)
    print(student.summary_report())


main()
