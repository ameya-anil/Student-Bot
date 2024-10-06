from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
students_file = 'students.json'

# Initialize the students.json file if it does not exist
if not os.path.exists(students_file):
    with open(students_file, 'w') as f:
        json.dump([], f)

# Load student data
def load_students():
    with open(students_file, 'r') as f:
        return json.load(f)

# Save student data
def save_students(data):
    with open(students_file, 'w') as f:
        json.dump(data, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    student = request.json
    students = load_students()
    students.append(student)
    save_students(students)
    return jsonify(success=True)

@app.route('/query', methods=['POST'])
def query():
    question = request.json['question'].lower()
    students = load_students()
    
    # Simple keyword matching to find the student
    response = "Sorry, I couldn't find that information."
    for student in students:
        if student['name'].lower() in question:
            response = f"Name: {student['name']}, Roll Number: {student['roll_number']}, Age: {student['age']}, Marks: {student['marks']}"
            break
    
    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True)
