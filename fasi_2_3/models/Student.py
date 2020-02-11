from datetime import date
import datetime

class Student:

    def __init__(self, firstname, lastname, birthdate, grades):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.grades = grades

    def age(self):
        today = date.today()
        birthdate = datetime.datetime.strptime(self.birthdate, '%Y-%m-%d').date()
        difference = today - birthdate
        return (int(difference.days / 365))

    def avg_grade(self, grades_array):
        if(len(grades_array) > 0):
            return (self.avg(grades_array))
        else:
            return 0

    def avg_grade2(self):
        if((self.grades != "") and (self.grades != None)):
            grades_array = self.grades.split(',')
            return (self.avg(grades_array))
        else:
            return 0

    def avg(self, grades_array):
        sum = 0
        for grade in grades_array:
            sum = sum + int(grade)
        return (sum / len(grades_array))

    def serialize(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "birthdate": self.birthdate,
            "grades": self.grades
        }

    def to_string(self):
        print("Profilo studente:")
        print("Nome: " + self.firstname + "\nCognome: " + self.lastname + "\nData di nascita: " + self.birthdate + "\nVoti: " + self.grades)
