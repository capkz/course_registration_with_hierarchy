from pydes2 import *
import sqlite3

k = des("SECURITY", "CBC", "\0\0\0\0\0\0\0\0",pad=None, padmode = PAD_PKCS5)
conn = sqlite3.connect('studentdatabase.db')
c = conn.cursor()

class Course:
    def __init__(self,coursename,department,courseinfo):
        self.coursename = k.encrypt(coursename)
        self.department = k.encrypt(department)
        self.courseinfo = k.encrypt(courseinfo)
        
        
#clinical = Course("Clinical","Psychology Department","This course is about clinical treatmens for patients")
clinical = Course("Algorithm","Computer Engineering","This course teaches all about algorithms and how to calculate the runtime.")
c.execute("INSERT INTO courses VALUES (?,?,?)",(clinical.coursename,clinical.department,clinical.courseinfo))
conn.commit()
conn.close()