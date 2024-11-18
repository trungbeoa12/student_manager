class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)
    
    def __str__(self):
        subject_list = ' ,'.join([subject.name for subject in self.subjects])
        return f"Student ID: {self.student_id}, name: {self.name}, subject: [{subject_list}]"
