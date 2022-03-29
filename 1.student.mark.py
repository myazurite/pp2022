students = []
courses = []
marks = []

def studentsNum():
    stt_total = int(input("Enter number of students in class: "))
    return stt_total

def studentInfoInput(stt_index):
    id = input(f"Enter student #{stt_index} id: ")
    name = input(f"Enter student #{stt_index} name: ")
    dob = input(f"Enter student #{stt_index} date of birth: ")
    stdInfo = {'id':id, 'name':name, 'DOB':dob}
    students.append(stdInfo)

def coursesNum():
    course_count = int(input("Enter number of courses: "))
    return course_count

def courseInfoInput(course_order):
    id = input(f"Enter course #{course_order} id: ")
    name = input(f"Enter course #{course_order} name: ")
    course_info = {'id':id,'name':name}
    courses.append(course_info)

def marking_process():
    print("Marking")
    for i in courses:
        while i:
            course_ID = input("Enter course id: ")
            crsID_list = [crs_Id["id"] for crs_Id in courses]
            if course_ID in crsID_list:
                for j in students:
                    while j:
                        stdID = input("Enter student id: ")
                        stdIDList = [std_Id["id"] for std_Id in students]
                        if stdID in stdIDList:
                            mark = round(float(input("Enter mark: ")), 2)
                            mrk = {'Student ID':stdID, 'Course ID':course_ID, 'Mark':mark}
                            marks.append(mrk)
                            break
                        else:
                            print("No result")
                break
            else:
                print("No result")

def displayStudents():
    print("Students List:")
    stt_index = 1
    for i in students:
        print(f"{stt_index}.")
        print(f"Student ID: {i.get('id')} \nStudent name: {i.get('name')} \nDate of birth: {i.get('DOB')}")
        stt_index += 1

def displayCourses():
    print("Courses List:")
    course_order = 1
    for i in courses:
        print(f"{course_order}.")
        print(f"Course ID: {i.get('id')} \nCourse name: {i.get('name')}")
        course_order += 1

def displayMarks():
    for i in marks:
        print(f"Student ID: {i.get('Student ID')} \nCourse ID: {i.get('Course ID')} \nMark: {i.get('Mark')}")

print("Student Mark Management\n")
stt_total = int(studentsNum())
for i in range(0,stt_total):
    studentInfoInput(i+1)
course_count = int(coursesNum())
for i in range(0,course_count):
    courseInfoInput(i+1)
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
        exit_option = input("Proceed to exit? [Y/N]: ")
        if exit_option.upper() == "Y":
            break
        else: pass
    else:
        print("Invalid input \n")




