from flask import Blueprint, render_template, request, redirect
from service.student_service import StudentService

student_bp = Blueprint('students', __name__)

service = StudentService()


@student_bp.route("/")
def index():
    students = service.list_students()
    return render_template("index.html", students=students)


@student_bp.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "age": request.form["age"],
            "course": request.form["course"]
        }

        service.create_student(data)

        return redirect("/")

    return render_template("add_student.html")


@student_bp.route("/edit/<id>", methods=["GET", "POST"])
def edit_student(id):

    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "age": request.form["age"],
            "course": request.form["course"]
        }

        service.update_student(id, data)

        return redirect("/")

    student = service.get_student(id)

    return render_template("edit_student.html", student=student)


@student_bp.route("/delete/<id>")
def delete_student(id):

    service.delete_student(id)

    return redirect("/")