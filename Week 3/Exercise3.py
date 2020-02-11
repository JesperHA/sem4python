import random
import csv

class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url
    
    def get_avg_grade(self):
  
        avg_grade = 0
        return avg_grade

class Data_sheet():
    def __init__(self, courses=[]):
        self.courses = courses
    
    def get_grades_as_list(self):
        grade_list = 0
        return grade_list

class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade



grades = [-3, 0, 2, 4, 7, 10, 12]
course1 = Course("Math", 3.114, "Flemming", 15, random.choice(grades))
course2 = Course("Physics", 3.113, "Karl", 10, random.choice(grades))
course3 = Course("Chemistry", 2.112, "Birger", 10, random.choice(grades))
course4 = Course("Medicin", 3.110, "Ulla", 15, random.choice(grades))

def random_generator(n):

    name = ["Jesper", "Ulrik", "Mathias", "Emil", "Karl"]
    gender = ["Male", "Female"]
    courses = [course1, course2, course3, course4]
    img_url = ["hej.com", "faggot.com"]


    file = open("students.csv", "w", newline="")
    writer = csv.writer(file)

    # with open("students.csv", "w", newline="") as file:
    #     writer = csv.writer(file)


    writer.writerow(["stud_name", "course_name", "teacher", "ECTS", "classroom", "grade", "img_url"])
   
    for element in range(n):
        ds = Data_sheet(random.sample(courses, 2))
        st = Student(random.choice(name), random.choice(gender), ds, random.choice(img_url))
        for i in range(2):
            if i == 0:
                writer.writerow([st.name, st.data_sheet.courses[i].name, st.data_sheet.courses[i].teacher, st.data_sheet.courses[i].ETCS, st.data_sheet.courses[i].classroom, st.data_sheet.courses[i].grade, st.image_url])
            elif i > 0:
                writer.writerow([".", st.data_sheet.courses[i].name, st.data_sheet.courses[i].teacher, st.data_sheet.courses[i].ETCS, st.data_sheet.courses[i].classroom, st.data_sheet.courses[i].grade, st.image_url])
  

random_generator(3)





