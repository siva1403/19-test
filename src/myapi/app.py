# from flask import Flask, jsonify
# from datetime import datetime

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return jsonify({
#         "message": "Python API is running",
#         "edited_by": "bharath",
#         "timestamp": datetime.now().strftime("%H:%M:%S %d %b %Y"),
#         "message": "edited by vijay"
#     })

# @app.route("/health")
# def health():
#     return jsonify({
#         "status": "UP"
#     })

# def main():
#     app.run(host="0.0.0.0", port=5000)

# if __name__ == "__main__":
#     main()


from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Bharath", "role": "Developer"},
    {"id": 2, "name": "Ravi", "role": "Tester"}
]

# GET all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

# GET employee by id
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    for emp in employees:
        if emp["id"] == id:
            return jsonify(emp)
    return jsonify({"message": "Employee not found"}), 404

# POST new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    employees.append(data)
    return jsonify({"message": "Employee added successfully"}), 201

# PUT update employee
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()

    for emp in employees:
        if emp["id"] == id:
            emp["name"] = data["name"]
            emp["role"] = data["role"]
            return jsonify({"message": "Employee updated successfully"})

    return jsonify({"message": "Employee not found"}), 404

# DELETE employee
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    for emp in employees:
        if emp["id"] == id:
            employees.remove(emp)
            return jsonify({"message": "Employee deleted successfully"})

    return jsonify({"message": "Employee not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
