import sqlite3
from pydes2 import *

columns = ["Name","Surname","Department","Advisor","Graduate Status","Monday","Tuesday","Wednesday","Thursday","Friday"]
k = des("SECURITY", "CBC", "\0\0\0\0\0\0\0\0",pad=None, padmode = PAD_PKCS5)
conn = sqlite3.connect('studentdatabase.db')
c = conn.cursor()

def getStudentRowDatabyName(stdname): #Get all the records of a student selected by decrypting all
    c.execute("SELECT Name FROM students")
    names = [item[0] for item in c.fetchall()]
    for x in range(len(names)):
        decryptedname = k.decrypt(names[x]).decode("utf-8")
        if(stdname == decryptedname):
            indexnum = x
    c.execute("SELECT * FROM students WHERE Name=?",(names[indexnum],))
    records = c.fetchone()
    return records

def getRowDatabyDepartment(department): #Get all the records of a student selected by Department
    c.execute("SELECT Department FROM students")
    names = [item[0] for item in c.fetchall()]
    for x in range(len(names)):
        decryptedname = k.decrypt(names[x]).decode("utf-8")
        if(department == decryptedname):
            indexnum = x
    c.execute("SELECT * FROM students WHERE Department=?",(names[indexnum],))
    records = [item[0] for item in c.fetchall()]
    decrypted = []
    for x in records:
        decrypted.append(k.decrypt(x).decode("utf-8"))
    return decrypted

def getAdvisorStudents(advisorname): #Get all the students of an advisor
    c.execute("SELECT Advisor FROM students")
    names = [item[0] for item in c.fetchall()]
    for x in range(len(names)):
        decryptedname = k.decrypt(names[x]).decode("utf-8")
        if(advisorname == decryptedname):
            indexnum = x
    c.execute("SELECT * FROM students WHERE Advisor=?",(names[indexnum],))
    records = [item[0] for item in c.fetchall()]
    decrypted = []
    for x in records:
        decrypted.append(k.decrypt(x).decode("utf-8"))
    return decrypted

def getAllStudents(): #Get all student names
    c.execute("SELECT Advisor FROM students")
    names = [item[0] for item in c.fetchall()]
    for x in range(len(names)):
        decryptedname = k.decrypt(names[x]).decode("utf-8")
    c.execute("SELECT * FROM students")
    records = [item[0] for item in c.fetchall()]
    decrypted = []
    for x in records:
        decrypted.append(k.decrypt(x).decode("utf-8"))
    return decrypted

def getCourseNamesbyDepartment(department): #Get all courses of a department
    c.execute("SELECT Department FROM courses")
    names = [item[0] for item in c.fetchall()]
    for x in range(len(names)):
        decryptedname = k.decrypt(names[x]).decode("utf-8")
        if(department == decryptedname):
            indexnum = x
    c.execute("SELECT * FROM courses WHERE Department=?",(names[indexnum],))
    records = [item[0] for item in c.fetchall()]
    decrypted = []
    for x in records:
        decrypted.append(k.decrypt(x).decode("utf-8"))
    return decrypted

def getCourseInfobyName(coursename): #Get Course information by its name
    print(coursename.title())
    c.execute("SELECT cName FROM courses")
    names = [item[0] for item in c.fetchall()]
    for x in range(len(names)):
        decryptedname = k.decrypt(names[x]).decode("utf-8")
        if(coursename == decryptedname):
            indexnum = x
    c.execute("SELECT Info FROM courses WHERE cName = ?",(names[indexnum],))
    records = c.fetchone()
    return k.decrypt(records[0]).decode("utf-8")

def getCourseRowDatabyName(course): #Get all course data by its name
    c.execute("SELECT cName FROM courses")
    names = [item[0] for item in c.fetchall()]
    for x in range(len(names)):
        decryptedname = k.decrypt(names[x]).decode("utf-8")
        if(course == decryptedname):
            indexnum = x
    c.execute("SELECT * FROM courses WHERE cName=?",(names[indexnum],))
    records = c.fetchone()
    return records


def setCourseInfo(course,newinfo): #change course info
    courserecord = getCourseRowDatabyName(course)
    c.execute("UPDATE courses SET Info = ? WHERE cName = ?",(k.encrypt(newinfo), courserecord[0]))
    conn.commit()


def getDepartmentalStudents(department): #Get all students of a department
    c.execute("SELECT Department FROM students")
    names = [item[0] for item in c.fetchall()]
    for x in range(len(names)):
        decryptedname = k.decrypt(names[x]).decode("utf-8")
        if(department == decryptedname):
            indexnum = x
    c.execute("SELECT * FROM students WHERE Department=?",(names[indexnum],))
    records = [item[0] for item in c.fetchall()]
    decrypted = []
    for x in records:
        decrypted.append(k.decrypt(x).decode("utf-8"))
    return decrypted

def getStudentRecord(stdname): #Get all records of a student
    studentrecord = getStudentRowDatabyName(stdname)
    print("")
    for x in range(0,5):
        if(x == 4):
            boolean = k.decrypt(studentrecord[x]).decode("utf-8")
            if(boolean == "0"):
                status = "No"
            else:
                status = "Yes"
            print(columns[x]+": "+status)
        else:
            print(columns[x]+": "+k.decrypt(studentrecord[x]).decode("utf-8"))
    print("")

def getStudentSchedule(stdname): #Get only the schedule of a student
    studentrecord = getStudentRowDatabyName(stdname)
    print("")
    for x in range(5,10):
        print(columns[x]+":\t"+k.decrypt(studentrecord[x]).decode("utf-8"))
    print("")
    
def confirmCourses(stdname):
    studentrecord = getStudentRowDatabyName(stdname)
    
def setStudentAdvisor(stdname,advisor): #Assign a advisor to a student
    studentrecord = getStudentRowDatabyName(stdname)
    updateTable = k.encrypt(advisor.title())
    c.execute("UPDATE students SET Advisor = ? WHERE Name = ?",(updateTable, studentrecord[0]))
    conn.commit()

def checkCoursesConfirmed(stdname): 
    studentrecord = getStudentRowDatabyName(stdname)
    isConfirmed = k.decrypt(studentrecord[10]).decode("utf-8")
    if (isConfirmed == "0"):
        print("\nThe courses are not confirmed, do you want to confirm?")
        sel = input("Type Yes or No to continue: ").title()
        if (sel == "Yes"):
            updateTable = k.encrypt("1")
            c.execute("UPDATE students SET isCoursesConfirmed = ? WHERE Name = ?",(updateTable, studentrecord[0]))
        elif (sel == "No"):
            print("Returning to menu")
        else:
            print("Invalid input.")
    elif (isConfirmed == "1"):
        print("The courses are confirmed. Do you want to revert the confirmation?")
        sel = input("Type Yes or No to continue: ").title()
        if (sel == "Yes"):
            updateTable = k.encrypt("0")
            c.execute("UPDATE students SET isCoursesConfirmed = ? WHERE Name = ?",(updateTable, studentrecord[0]))
        elif (sel == "No"):
            print("Returning to menu")
        else:
            print("Invalid input.")
    conn.commit()
