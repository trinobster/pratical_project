import importlib.util
from models.Student import Student

def main():
    grades_array = [25, 30, 18, 23]
    grades = ','.join(map(str, grades_array))

    s1 = Student("John", "Bing", "1992-08-26", grades)

    s1.to_string()
    print("Età: " + str(s1.age()))

    print("Media voti avg_grade: " + str(s1.avg_grade(grades_array)))
    print("Media voti avg_grade2: " + str(s1.avg_grade2()))

if __name__== "__main__":
    main()
