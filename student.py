class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.subjects = []  # Danh sách môn học mà học sinh đang học

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "subjects": self.subjects
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data["student_id"], data["name"])
        student.subjects = data["subjects"]
        return student

