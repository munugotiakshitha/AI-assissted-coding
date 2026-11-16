from flask import Flask, request, jsonify

app = Flask(__name__)
students = []


def next_id():
    return max((student["id"] for student in students), default=0) + 1


@app.get("/students")
def list_students():
    """Return all student records."""
    return jsonify(students), 200


@app.post("/students")
def add_student():
    """Add a student using JSON fields: name, age, and course."""
    data = request.get_json(silent=True) or {}

    if not data.get("name"):
        return jsonify({"error": "Student name is required"}), 400

    student = {
        "id": next_id(),
        "name": data["name"],
        "age": data.get("age"),
        "course": data.get("course"),
    }
    students.append(student)
    return jsonify(student), 201


@app.put("/students/<int:student_id>")
def update_student(student_id):
    """Update the supplied fields for a student."""
    student = next(
        (item for item in students if item["id"] == student_id),
        None,
    )
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json(silent=True) or {}
    for field in ("name", "age", "course"):
        if field in data:
            student[field] = data[field]

    return jsonify(student), 200


@app.delete("/students/<int:student_id>")
def delete_student(student_id):
    """Delete a student by ID."""
    student = next(
        (item for item in students if item["id"] == student_id),
        None,
    )
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    students.remove(student)
    return jsonify({"message": "Student deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True) 