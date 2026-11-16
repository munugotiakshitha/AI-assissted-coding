from flask import Flask, request, jsonify

app = Flask(__name__)
employees = []


def next_id():
    return max((employee["id"] for employee in employees), default=0) + 1


def valid_salary(value):
    """Convert a salary to a non-negative number, or return None."""
    try:
        salary = float(value)
        return salary if salary >= 0 else None
    except (TypeError, ValueError):
        return None


@app.get("/employees")
def list_employees():
    """Return all employees and their salary details."""
    return jsonify(employees), 200


@app.post("/employees")
def add_employee():
    """Add an employee using JSON fields: name, role, and salary."""
    data = request.get_json(silent=True) or {}

    if not data.get("name") or "salary" not in data:
        return jsonify({"error": "Employee name and salary are required"}), 400

    salary = valid_salary(data["salary"])
    if salary is None:
        return jsonify({"error": "Salary must be a non-negative number"}), 400

    employee = {
        "id": next_id(),
        "name": data["name"],
        "role": data.get("role"),
        "salary": salary,
    }
    employees.append(employee)
    return jsonify(employee), 201


@app.put("/employees/<int:employee_id>/salary")
def update_salary(employee_id):
    """Update the salary for one employee."""
    employee = next(
        (item for item in employees if item["id"] == employee_id),
        None,
    )
    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json(silent=True) or {}
    if "salary" not in data:
        return jsonify({"error": "Salary is required"}), 400

    salary = valid_salary(data["salary"])
    if salary is None:
        return jsonify({"error": "Salary must be a non-negative number"}), 400

    employee["salary"] = salary
    return jsonify(employee), 200


@app.delete("/employees/<int:employee_id>")
def delete_employee(employee_id):
    """Delete an employee by ID."""
    employee = next(
        (item for item in employees if item["id"] == employee_id),
        None,
    )
    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    employees.remove(employee)
    return jsonify({"message": "Employee deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)