from school_manager import SchoolManager
from student import Student
from subject import Subject

def main():
    manager = SchoolManager()

    # Tải dữ liệu từ file JSON
    filename = "school_data.json"
    manager.load_from_file(filename)

    # Thêm dữ liệu nếu cần
    manager.add_student(Student(1, "Nguyen Van A"))
    manager.add_student(Student(2, "Le Thi B"))

    manager.add_subject(Subject(101, "Toan"))
    manager.add_subject(Subject(102, "Van"))

    # Gán môn học
    manager.assign_subject_to_student(1, 101)
    manager.assign_subject_to_student(1, 102)
    manager.assign_subject_to_student(2, 101)

    print("Danh sách học sinh:")
    manager.show_student()

    # Lưu dữ liệu vào file JSON
    manager.save_to_file(filename)

if __name__ == '__main__':
    main()

