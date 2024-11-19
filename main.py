from school_manager import SchoolManager
from student import Student
from subject import Subject

def main():
    manager = SchoolManager()
    filename = "school_data.json"
    manager.load_from_file(filename)

    while True:
        print("\n=== Quản lý Trường Học ===")
        print("1. Thêm học sinh")
        print("2. Thêm môn học")
        print("3. Gán môn học cho học sinh")
        print("4. Hiển thị danh sách học sinh")
        print("5. Hiển thị danh sách môn học")
        print("6. Hiển thị chi tiết học sinh và môn học")
        print("7. Thống kê số lượng môn học của mỗi học sinh")
        print("8. Hiển thị danh sách học sinh theo môn học")
        print("9. Lưu dữ liệu")
        print("10. Thoát")
        choice = input("Chọn chức năng (1-10): ")

        if choice == '1':
            try:
                student_id = int(input("Nhập ID học sinh: "))
                name = input("Nhập tên học sinh: ")
                manager.add_student(Student(student_id, name))
                print("Học sinh đã được thêm thành công!")
            except ValueError:
                print("ID phải là một số!")
        elif choice == '2':
            try:
                subject_id = int(input("Nhập ID môn học: "))
                name = input("Nhập tên môn học: ")
                manager.add_subject(Subject(subject_id, name))
                print("Môn học đã được thêm thành công!")
            except ValueError:
                print("ID phải là một số!")
        elif choice == '3':
            try:
                student_id = int(input("Nhập ID học sinh: "))
                subject_id = int(input("Nhập ID môn học: "))
                manager.assign_subject_to_student(student_id, subject_id)
                print("Môn học đã được gán thành công!")
            except ValueError:
                print("ID phải là một số!")
        elif choice == '4':
            print("\nDanh sách học sinh:")
            manager.show_student()
        elif choice == '5':
            print("\nDanh sách môn học:")
            for subject in manager.subjects:
                print(f"ID: {subject.subject_id}, Tên: {subject.name}")
        elif choice == '6':
            print("\nChi tiết học sinh và môn học:")
            manager.show_students_with_subjects()
        elif choice == '7':
            manager.show_student_subject_count()
        elif choice == '8':
            try:
                subject_id = int(input("Nhập ID môn học: "))
                manager.show_students_by_subject(subject_id)
            except ValueError:
                print("ID phải là một số!")
        elif choice == '9':
            manager.save_to_file(filename)
        elif choice == '10':
            manager.save_to_file(filename)
            print("Đã lưu dữ liệu và thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == '__main__':
    main()

