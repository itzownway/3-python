from flask import Flask, jsonify
from flask_cors import CORS
from controller.student_controller import student_bp

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Student CRUD Flask backend is running successfully.",
        "project": "React + Flask + MongoDB",
        "available_api": "http://127.0.0.1:5000/api/students/",
        "steps": [
            "1. Start MongoDB service",
            "2. Run Flask backend from backend folder",
            "3. Run React frontend from frontend folder",
            "4. Open frontend in browser",
            "5. Use /api/students/ for backend API testing"
        ]
    }), 200

app.register_blueprint(student_bp, url_prefix="/api/students")

if __name__ == "__main__":
    app.run(debug=True)