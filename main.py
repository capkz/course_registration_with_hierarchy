import os
import sqlite3
from pydes2 import *
import sysadmin

users = ["Student", "Graduate" "Student", "Academic" "Advisor", "Vice Chair", "Dean", "Rector"]
while(1):
    os.system("cls")
    print("\t\t\t~~Login Screen~~")
    print("Select an User to continue:\n1)Student\n2)Graduate Student\n3)Academic Advisor\n4)Vice Chair")
    print("5)Dean\n6)Rector")
    userNum = input("Type the number corresponding to the user: ")
    os.system("cls")
    print("\t\t\t~~"+users[int(userNum)-1]+"~~")
    print("Here are the things you can do on this user:")

    if userNum == "1": #Student
        print("You can only take 3-5 courses.\nCagil\nGoktug\nAli")
        stdlogin = input("Type in the one of the student names above to log in: ").lower()
        os.system("cls")
        print("\t\t\t~~Student Page~~")
        if(stdlogin == "cagil" or stdlogin == "ali"):
            stdlogin = stdlogin.title()
            print("Welcome "+stdlogin+", here are the things you can do:\n1)View your records\n2)View Courses")
            sel = input("Enter a number to continue: ")
            if( sel == "1"):
                sysadmin.getStudentRecord(stdlogin)
            elif( sel == "2"):
                sysadmin.getStudentSchedule(stdlogin)
            input("Press enter to return to main menu:")
        
    elif userNum == "2": #Graduate Student
        print("You can only take 7 courses.\nGoktug")
        login = input("Type in the one of the student names above to log in: ").lower()
        os.system("cls")
        print("\t\t\t~~Student Page~~")
        if(login == "goktug"):
            login = login.title()
            print("Welcome "+login+", here are the things you can do:\n1)View your records\n2)View Courses")
            sel = input("Enter a number to continue: ")
            if( sel == "1"):
                sysadmin.getStudentRecord(login)
            elif( sel == "2"):
                sysadmin.getStudentSchedule(login)
            input("Press Enter to return to main menu...")
    
    elif userNum == "3": #Academic Advisor
        print("Duygu Buyuk\nDogu Erdener")
        login = input("Type in one of the advisor's name to log in: ").title()
        os.system('cls')
        print("\t\t\t~~Academic Advisor~~")
        if(login=="Duygu Buyuk" or login =="Dogu Erdener"):
            login = login.title()
            print("Welcome "+login+". Here are your students:")
            advisorstudents = sysadmin.getAdvisorStudents(login)
            for x in advisorstudents:
                print(x)
            sel = input("\nEnter a student's name to continue: ").title()
            if(sel in advisorstudents):
                print("Welcome to "+sel+"'s page. What do you want to do?")
                print("1)View assigned student's records\n2)Confirm their courses")
                numb = input("Enter a number to proceed: ")
                if(numb == "1"):
                    sysadmin.getStudentRecord(sel)
                elif(numb == "2"):
                    sysadmin.checkCoursesConfirmed(sel)
                else:
                    print("Wrong input")
        sysadmin.getAdvisorStudents("Duygu Buyuk")
        input("Press Enter to return to main menu...")
    
    elif userNum == "4": #Vice Chair
        courses = sysadmin.getCourseNamesbyDepartment("Computer Engineering")

        print("Welcome. Here are the things you can do\n1)Edit/View Departmental Courses\n2)Assign Advisor\n3)Access Students")
        numb = input("Enter a number to continue: ")
        if(numb=="1"):
            print("\nHere are the things you can do:\n1)Edit Departmental Course\n2)View Departmental Course Info")
            numb = input("Enter a number to continue: ")
            if(numb=="1" or numb=="2"):
                print("\nHere are the courses you can work on:")
                for x in courses:
                    print(x)
                    
                if(numb=="1"):
                    select = input("Type in the course you want to change info of: ").title()
                    if(select in courses):
                        newinfo = input("Enter the new course description: ")
                        sysadmin.setCourseInfo(select, newinfo)
                            
                elif(numb=="2"):
                    select = input("Type in a course to continue: ").title()
                    if(select in courses):
                        print(sysadmin.getCourseInfobyName(select))
            else:
                print("Invalid Input")

        elif(numb=="2"):
            print("Here are the students you can assign Advisor to:")
            departmentalStudents = sysadmin.getDepartmentalStudents("Computer Engineering")
            for x in departmentalStudents:
                print(x)
            sel = input("\nEnter a student's name to continue: ").title()
            if(sel in departmentalStudents):     
                assignedadvisor = input("Enter the advisor's name: ")      
                sysadmin.setStudentAdvisor(sel, assignedadvisor)
        
        elif(numb=="3"):
            print("Here are the students you have access to:")
            departmentalStudents = sysadmin.getDepartmentalStudents("Computer Engineering")
            for x in departmentalStudents:
                print(x)
            sel = input("\nEnter a student's name to continue: ").title()
            if(sel in departmentalStudents):
                print("Welcome to "+sel+"'s page. What do you want to do?")
                print("1)View department students' records\n2)Confirm courses")
                numb = input("Enter a number to continue: ")
                if(numb=="1"):
                    sysadmin.getStudentRecord(sel)
                elif(numb=="2"):
                    sysadmin.checkCoursesConfirmed(sel)
                else:
                    print("Invalid Input.")
        else:
            print("Invalid Input.")
        input("Press Enter to return to main menu...")
        
    elif userNum == "5": #Dean
        departmentalStudents = sysadmin.getDepartmentalStudents("Computer Engineering")
        for x in departmentalStudents:
            print(x)
        select = input("Enter the name of student to view their records: ").title()
        if(select in departmentalStudents):
            sysadmin.getStudentRecord(select)
        input("Press Enter to return to main menu...")
    elif userNum == "6": #Rector
        studentslist = sysadmin.getAllStudents()
        for x in studentslist:
            print(x)
        sel = input("Type the name of the student to view their records: ").title()
        if(sel in studentslist):
            print("")
            sysadmin.getStudentRecord(sel)
        else:
            print("Invalid Student.")
        input("Press Enter to return to main menu...")