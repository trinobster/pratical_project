import flask
from flask import request, jsonify
import json
import importlib.util
from models.Student import Student

app = flask.Flask(__name__)
app.config["DEBUG"] = True

students = []

# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/get_students', methods=['GET'])
def get_students():
    return "1"

@app.route('/create_student', methods=['POST'])
def create_student():
    s1 = Student("John", "Bing", "1992-08-26", "23, 23")
    parsed_data = json.loads(request.data)
    return parsed_data

app.run()
