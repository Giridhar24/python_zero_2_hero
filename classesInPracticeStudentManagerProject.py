# Topic of the Day: Classes in Practice (Student Manager Project)
# Explanation: Let's upgrade our "Student Manager" from Day 15.
# Instead of random print statements, we will create a Student class to hold data cleanly. This is how real apps structure data.

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | GPA: {self.get_average():.2f}"

# Usage
s1 = Student(101, "Alice")
s1.add_grade(90)
s1.add_grade(80)

print(s1)  # Uses the __str__ method to print cleanly