class student:
    def __init__(self,id,name,dob):
        self._id = id
        self._name = name
        self._dob = dob
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_dob(self):
        return self._dob
    def __str__(self):
        return f"Student ID: {self._id} \nStudent Name: {self._name} \nStudent DOB:{self._dob}"

class course:
    def __init__(self,id,name):
        self._id = id
        self._name = name
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def __str__(self):
        return f"Course ID: {self._id} \nCourse Name: {self._name}"

class mark:
    def __init__(self,std_id,crs_id,grade):
        self._std_id = std_id
        self._crs_id = crs_id
        self._grade = grade
    def get_std_id(self):
        return self._std_id
    def get_crs_id(self):
        return self._crs_id
    def get_grade(self):
        return self._grade

students = []
courses = []
marks = []

def studentsNum():
    stt_total = int(input("Enter number of students in class: "))
    return stt_total

def studentInfoInput(student_order):
    id = input(f"Enter student #{student_order} id: ")
    name = input(f"Enter student #{student_order} name: ")
    dob = input(f"Enter student #{student_order} date of birth: ")
    stdInfo = student(id,name,dob)
    students.append(stdInfo)

def coursesNum():
    course_count = int(input("Enter number of courses: "))
    return course_count

def courseInfoInput(course_order):
    id = input(f"Enter course #{course_order} id: ")
    name = input(f"Enter course #{course_order} name: ")
    course_info = course(id,name)
    courses.append(course_info)

def marking_process():
    print("Marking:")
    for i in courses:
        while i:
            course_ID = input("Enter course id: ")
            crsID_list = [crs_Id.get_id() for crs_Id in courses]
            if course_ID in crsID_list:
                for j in students:
                    while j:
                        stdID = input("Enter student id: ")
                        stdIDList = [std_Id.get_id() for std_Id in students]
                        if stdID in stdIDList:
                            grade = round(float(input("Enter mark: ")), 1)
                            mrk = mark(stdID,course_ID,grade)
                            marks.append(mrk)
                            break
                        else:
                            print("No result")
                break
            else:
                print("No result")

def displayStudents():
    print("Students List:")
    student_order = 1
    for i in students:
        print(f"{student_order}.")
        print(i)
        student_order+=1

def displayCourses():
    print("Courses List:")
    course_order = 1
    for i in courses:
        print(f"{course_order}.")
        print(i)
        course_order += 1

def displayMarks():
    print("Student's mark:")
    for i in courses:
        print(f"Course ID: {i.get_id()}")
        for k in range(0,len(marks)):
            if(marks[k].get_crs_id() == i.get_id()):
                print(f"Student ID: {marks[k].get_std_id()} || Mark: {marks[k].get_grade()}")

print("Student Mark Management\n")
stt_total = int(studentsNum())
for i in range(0,stt_total):
    studentInfoInput(i + 1)
course_count = int(coursesNum())
for i in range(0,course_count):
    courseInfoInput(i + 1)
marking_process()

while 1:
    print("Class Info:")
    print("1. Display all students")
    print("2. Display all courses")
    print("3. Display marks")
    print("4. Exit")
    option = int(input("Enter your option: "))
    if option == 1:
        displayStudents()
    elif option == 2:
        displayCourses()
    elif option == 3:
        displayMarks()
    elif option == 4:
        exit_option = input("Proceed to  exit? [Y/N]: ")
        if exit_option.upper() == "Y":
            break
        else:
            pass
    else:
        print("Invalid input \n")




