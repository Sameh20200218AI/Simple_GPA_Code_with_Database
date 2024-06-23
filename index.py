class Course :
    def __init__(self) :
        self.course_name = input('Enter Course Name :')
        self.course_id = int(input('Enter Course ID :'))
        self.course_hours = int(input('Enter Course Hours :'))
        while self.course_hours <0 or self.course_hours>3:
            self.course_hours = int(input('Enter Course Hours again :'))

        self.course_marks = int(input('Enter Course Marks :'))
        while self.course_marks <0 or self.course_marks>100:
            self.course_marks = int(input('Enter Course Marks again :'))
        self.course_grade = ""
    def set_grade(self,marks):
        if (self.course_marks >=90):
            self.course_grade = 'A+'

        elif (self.course_marks >=85):
            self.course_grade = 'A'

        elif (self.course_marks >=80) :
            self.course_grade = 'B+'

        elif (self.course_marks >=75):
            self.course_grade = 'B'

        elif (self.course_marks >=70):
            self.course_grade = 'C+'

        elif (self.course_marks >=65):
            self.course_grade = 'C'

        elif (self.course_marks >=60):
            self.course_grade = 'D+'

        elif (self.course_marks >=50):
            self.course_grade = 'D'

        else :
            self.course_grade ='F'
    def Get_Points_of_Grade(self):
        if (self.course_grade=='A+'):
            return 4
        elif (self.course_grade=='A'):
            return 3.7
        elif (self.course_grade=='B+'):
            return 3.3
        elif (self.course_grade=='B'):
            return 3
        elif (self.course_grade=='C+'):
            return 2.7
        elif (self.course_grade=='C'):
            return 2.4
        elif (self.course_grade=='D+'):
            return 2.2
        elif (self.course_grade=='D'):
            return 2 
        else :
            return 0
class Student :
    def __init__(self,student_id,student_name,student_department):
        self.student_id = student_id
        self.student_name = student_name
        self.student_department = student_department
        self.courses = []
        self.student_gpa =None
    def add_course(self):
        c = Course()
        c.set_grade(c.course_marks)
        self.courses.append(c)


    def display_info_student(self):
        print('Name of student : ' , self.student_name)
        print('ID of student : ' , self.student_id)
        print('Department of student : ' , self.student_department)
        print('GPA of the student : ' , self.student_gpa)
        print(' ')

    def display_courses(self):
        for i in range(len(self.courses)): 
            print ('For ',i+1 , " course")
            print('----------------')
            print()
            print('Name of Course : ',self.courses[i].course_name)
            print('ID of Course : ',self.courses[i].course_id)
            print('Hours of Course : ',self.courses[i].course_hours)
            print('Grade of Course : ',self.courses[i].course_grade)
            print('')
    def total_hours(self):
        sum = 0
        for i in range (len(self.courses)):
            sum =sum+ self.courses[i].course_hours
        return sum
    def total_points(self):
        sum = 0.0
        for i in range (len(self.courses)):
            sum =sum + self.courses[i].course_hours* self.courses[i].Get_Points_of_Grade()
        return sum
    def calculate_gpa (self):
        self.student_gpa = self.total_points() / self.total_hours()
        return self.student_gpa
id = int(input('Enter id of the student : '))
name = input('Enter name of the student : ')
department = input('Enter department of the student : ')
gpa = None
s = Student(id,name,department)
num_of_courses = input('Enter the number of courses : ')
for i in range (int(num_of_courses)):
     print ('For ',i+1 , " st course")
     print('----------------')
     s.add_course()
gpa = s.calculate_gpa()
s.display_info_student()
print('')

# use database sql


import sqlite3 as sq 
db = sq.connect("info.db")
cr = db.cursor()
cr.execute("CREATE table if not exists Student(ID integer primary key,Name_ varchar(50),Department varchar(3),GPA float )")

cr.execute("insert into Student (ID,Name_,Department,GPA)values(?,?,?,?)",(id,name,department,gpa))
cr.execute("select * from Student")
print(cr.fetchall())


db.commit()
db.close()




