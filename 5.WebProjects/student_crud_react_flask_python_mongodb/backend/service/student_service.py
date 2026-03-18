from repository.student_repository import StudentRepository
from model.student_model import Student


class StudentService:
    def __init__(self):
        self.repo = StudentRepository()

    def create_student(self, data):
        student = Student(
            data["name"],
            data["age"],
            data["course"]
        )
        return self.repo.add_student(student.to_dict())

    def list_students(self):
        return self.repo.get_students()

    def get_student(self, student_id):
        return self.repo.get_student(student_id)

    def update_student(self, student_id, data):
        student = Student(
            data["name"],
            data["age"],
            data["course"]
        )
        return self.repo.update_student(student_id, student.to_dict())

    def delete_student(self, student_id):
        return self.repo.delete_student(student_id)