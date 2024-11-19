import json
from student import Student
from subject import Subject

class SchoolManager:
    def __init__(self):
        self.students = []  # Danh sách học sinh
        self.subjects = []  # Danh sách môn học

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def assign_subject_to_student(self, student_id, subject_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        subject = next((s for s in self.subjects if s.subject_id == subject_id), None)
        if student and subject:
            student.subjects.append(subject_id)
        else:
            print("Học sinh hoặc môn học không tồn tại!")

    def show_student(self):
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, Subjects: {student.subjects}")

    def save_to_file(self, filename):
        data = {
            "students": [student.to_dict() for student in self.students],
            "subjects": [subject.to_dict() for subject in self.subjects]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Dữ liệu đã được lưu vào file {filename}.")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.students = [Student.from_dict(s) for s in data["students"]]
            self.subjects = [Subject.from_dict(s) for s in data["subjects"]]
            print(f"Dữ liệu đã được tải từ file {filename}.")
        except FileNotFoundError:
            print(f"File {filename} không tồn tại. Bắt đầu với dữ liệu trống.")

