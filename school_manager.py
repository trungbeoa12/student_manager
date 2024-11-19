from student import Student
from subject import Subject

class SchoolManager:
    def __init__(self):
        self.students = {}
        self.subjects = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_subject(self, subject):
        self.subjects[subject.subject_id] = subject

    def assign_subject_to_student(self, student_id, subject_id):
        if student_id in self.students and subject_id in self.subjects:
            student = self.students[student_id]
            subject = self.subjects[subject_id]
            student.add_subject(subject)
        else:
            print("Invalid student of subject ID")

    def show_student(self):
        for student in self.students.values():
            print(student)
