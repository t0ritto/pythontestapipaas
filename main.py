from flask import Flask, jsonify, request

app = Flask(__name__)

# This is our data structure, a list of dictionaries
# In a real-life scenario, this would be a database
students = [
    {"id": 1, "name": "John", "course": "Physics"},
    {"id": 2, "name": "Sarah", "course": "Chemistry"},
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({"students": students})

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student is not None:
        return jsonify({"student": student})
    else:
        return {"error": "student not found"}, 404

@app.route('/students', methods=['POST'])
def create_student():
    new_student = request.get_json()
    students.append(new_student)
    return jsonify({"student": new_student}), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student is not None:
        updated_student = request.get_json()
        student.update(updated_student)
        return jsonify({"student": student})
    else:
        return {"error": "student not found"}, 404

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    return {"result": "student deleted"}

if __name__ == "__main__":
    app.run(debug=True)
