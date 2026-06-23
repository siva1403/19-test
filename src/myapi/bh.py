# names=[]
# numbers=[]
# list=['bharath',23,'ravi',45,'raju',78]
# for i in list:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append(i) 
# print("separation of names are:",names)
# print("separation of numbers are:",numbers)


from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Bharath", "role": "Developer"},
    {"id": 2, "name": "Ravi", "role": "Tester"},
    {"id": 3, "name": "siva", "role": "Tester"}
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
