from bson.objectid import ObjectId
from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
students_collection = db[COLLECTION_NAME]


class StudentRepository:
    def add_student(self, student_data):
        result = students_collection.insert_one(student_data)
        return str(result.inserted_id)

    def get_students(self):
        students = list(students_collection.find())

        for student in students:
            student["_id"] = str(student["_id"])

        return students

    def get_student(self, student_id):
        try:
            student = students_collection.find_one({"_id": ObjectId(student_id)})
            if student:
                student["_id"] = str(student["_id"])
            return student
        except Exception:
            return None

    def update_student(self, student_id, data):
        try:
            result = students_collection.update_one(
                {"_id": ObjectId(student_id)},
                {"$set": data}
            )
            return result.matched_count > 0
        except Exception:
            return False

    def delete_student(self, student_id):
        try:
            result = students_collection.delete_one({"_id": ObjectId(student_id)})
            return result.deleted_count > 0
        except Exception:
            return False