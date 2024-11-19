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
            
            
    def show_students_with_subjects(self):
        if not self.students:
            print("Chưa có học sinh nào trong danh sách.")
            return
        for student in self.students:
            subject_names = [sub.name for sub in self.subjects if sub.subject_id in student.subjects]
            print(f"ID: {student.student_id}, Name: {student.name}, Subjects: {', '.join(subject_names) if subject_names else 'Chưa đăng ký môn học nào'}")
            
    def show_student_subject_count(self):
        if not self.students:
            print("Chưa có học sinh nào trong danh sách.")
            return
        print("\nSố lượng môn học của mỗi học sinh:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, Số môn học: {len(student.subjects)}")
            
    def show_students_by_subject(self, subject_id):
        subject = next((s for s in self.subjects if s.subject_id == subject_id), None)
        if not subject:
            print(f"Môn học với ID {subject_id} không tồn tại.")
            return

        print(f"\nDanh sách học sinh học môn {subject.name}:")
        students_in_subject = [student for student in self.students if subject_id in student.subjects]
        if not students_in_subject:
            print("Không có học sinh nào học môn này.")
        else:
            for student in students_in_subject:
                print(f"ID: {student.student_id}, Name: {student.name}")




