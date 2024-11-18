class Subject:
    def __init__(self, subject_id, name):
        self.subject_id = subject_id
        self.name = name
    
    def __str__(self):
        return f"Subject_ID: {self.subject_id}, Name: {Self.name}"
