from flask import Blueprint, jsonify, request
from service.student_service import StudentService

student_bp = Blueprint("students", __name__)
service = StudentService()


@student_bp.route("/", methods=["GET"])
def get_students():
    students = service.list_students()
    return jsonify(students), 200


@student_bp.route("/<student_id>", methods=["GET"])
def get_student(student_id):
    student = service.get_student(student_id)

    if not student:
        return jsonify({"message": "Student not found"}), 404

    return jsonify(student), 200


@student_bp.route("/", methods=["POST"])
def add_student():
    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body is required"}), 400

    name = data.get("name", "").strip()
    age = data.get("age")
    course = data.get("course", "").strip()

    if not name or not age or not course:
        return jsonify({"message": "Name, age, and course are required"}), 400

    student_id = service.create_student({
        "name": name,
        "age": age,
        "course": course
    })

    return jsonify({
        "message": "Student created successfully",
        "student_id": student_id
    }), 201


@student_bp.route("/<student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body is required"}), 400

    name = data.get("name", "").strip()
    age = data.get("age")
    course = data.get("course", "").strip()

    if not name or not age or not course:
        return jsonify({"message": "Name, age, and course are required"}), 400

    updated = service.update_student(student_id, {
        "name": name,
        "age": age,
        "course": course
    })

    if not updated:
        return jsonify({"message": "Student not found"}), 404

    return jsonify({"message": "Student updated successfully"}), 200


@student_bp.route("/<student_id>", methods=["DELETE"])
def delete_student(student_id):
    deleted = service.delete_student(student_id)

    if not deleted:
        return jsonify({"message": "Student not found"}), 404

    return jsonify({"message": "Student deleted successfully"}), 200