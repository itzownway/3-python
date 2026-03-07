from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME
from bson.objectid import ObjectId

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
students = db[COLLECTION_NAME]


class StudentRepository:

    def add_student(self, student_data):
        return students.insert_one(student_data)

    def get_students(self):
        return list(students.find())

    def get_student(self, student_id):
        return students.find_one({"_id": ObjectId(student_id)})

    def update_student(self, student_id, data):
        return students.update_one(
            {"_id": ObjectId(student_id)},
            {"$set": data}
        )

    def delete_student(self, student_id):
        return students.delete_one({"_id": ObjectId(student_id)})