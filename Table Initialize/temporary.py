from pydes2 import *
import sqlite3

k = des("SECURITY", "CBC", "\0\0\0\0\0\0\0\0",pad=None, padmode = PAD_PKCS5)
class Student:
    def __init__(self,name, surname, department, advisor, isGraduate):
        self.name = k.encrypt(name)
        self.surname = k.encrypt(surname)
        self.department = k.encrypt(department)
        self.advisor = k.encrypt(advisor)
        self.isGraduate = k.encrypt(isGraduate)
    def monday(self,lectures):
        self.monday = k.encrypt(lectures)
    def tuesday(self,lectures):
        self.tuesday = k.encrypt(lectures)
    def wednesday(self,lectures):
        self.wednesday = k.encrypt(lectures)
    def thursday(self,lectures):
        self.thursday = k.encrypt(lectures)
    def friday(self,lectures):
        self.friday = k.encrypt(lectures)

std = Student("Ali","Hamdan","Computer Engineering","Duygu Buyuk", "0")
#std = Student("Goktug","Uysal","Psychology Department","Dogu Erdener", "1")
#std = Student("Cagil","Pekoz","Computer Engineering","Duygu Buyuk", "0")
std.monday("Network,Network,UE1,UE1")
std.tuesday("Java,Java,Algorithm,Algorithm")
std.wednesday("Java,Java,Algorithm,Algorithm")
std.thursday("None,None,Network,Network")
std.friday("Java,Java,Network,Network")

conn = sqlite3.connect('studentdatabase.db')
c = conn.cursor()

c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(std.name, std.surname, 
                                                                       std.department, std.advisor, 
                                                                       std.isGraduate, std.monday, 
                                                                       std.tuesday, std.wednesday, 
                                                                       std.thursday, std.friday))
conn.commit()
conn.close()

    



#plain = d.decrypt(key,ciphered,padding=True)

