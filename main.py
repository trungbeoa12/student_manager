from school_manager import SchoolManager
from student import Student
from subject import Subject

def main():
    manager = SchoolManager()

    # them hoc sinh
    manager.add_student(Student(1, "Nguyen Van A"))
    manager.add_student(Student(2, "Le Thi B"))

    # Them Mon hoc
    manager.add_subject(Subject(101, "Toan"))
    manager.add_subject(Subject(102, "Van"))

    # gan mon cho hoc sinh
    manager.assign_subject_to_student(1, 101)
    manager.assign_subject_to_student(1, 102)
    manager.assign_subject_to_student(2, 101)

    print("Danh sach hoc sinh")
    manager.show_student()

if __name__ == '__main__':
    main()
