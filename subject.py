class Subject:
    def __init__(self, subject_id, name):
        self.subject_id = subject_id
        self.name = name

    def to_dict(self):
        return {
            "subject_id": self.subject_id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["subject_id"], data["name"])

