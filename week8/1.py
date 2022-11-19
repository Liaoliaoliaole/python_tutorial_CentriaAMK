#Student - Course (association class needed)
import numpy as np

class Student:
    def __init__(self, name, id, number, course):
        self.name = name
        self.id = id
        self.number = number
        self.course = course

    def addCourse(self, newcourse):
        self.course.append(newcourse)

    def getInfo(self):
        print("=" * 30)
        print("The information of this student: ")
        print("=" * 30)
        print("Name: ", self.name)
        print("ID: ", self.id)
        print("Student Number: ", self.number)
        print("Course: ", self.course)

class Course:
	def __init__(self, index, courseName):
		self.index = index
		self.courseName = courseName

	def getInfo(self):
		print("=" * 30)
		print("The information of this course: ")
		print("=" * 30)
		print("The index of this course is ", self.index)
		print("The name of this course is ", self.courseName)


#data
#create the student's information
student = []
for i in range(20):
	k = Student("student"+str(i+1), i+1, 22*100000000+(i+4)*100+(i+3)*10+i, [])
	student.append(k)

#create the course infomation
course = []
course1 = Course(1, "numbericalAnalysis")
course.append(course1)
course2 = Course(2, "database")
course.append(course2)
course3 = Course(3, "advancedProgramming")
course.append(course3)
course4 = Course(4, "python")
course.append(course4)
course5 = Course(5, "linux")
course.append(course5)
course6 = Course(6, "FinnishLanguage")
course.append(course6)

#random arrange three course for each student
def ranCourse(student, course):
	for i in range(20):
		c = np.random.choice(course, 3)
		for j in range(3):
			student[i].addCourse(c[j].courseName)

ranCourse(student, course)
#print information
for i in range(20):
	student[i].getInfo()


