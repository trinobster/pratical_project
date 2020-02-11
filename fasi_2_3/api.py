import flask
from flask import request, jsonify
import json
import importlib.util
from models.Student import Student

app = flask.Flask(__name__)
app.config["DEBUG"] = True

students = []

@app.route('/get_students', methods=['GET'])
def get_students():
    return {
        "students": students
    }

@app.route('/create_student', methods=['POST'])
def create_student():
    parsed_data = json.loads(request.data)
    if((parsed_data['firstname'] == "")  or (parsed_data['lastname'] == "")  or (parsed_data['birthdate'] == "") or (parsed_data['grades'] == "") ):
        return "false"
    else:
        new_student = Student(parsed_data['firstname'], parsed_data['lastname'], parsed_data['birthdate'], parsed_data['grades'])
        students.append(new_student.serialize())
        return "true"


app.run()
