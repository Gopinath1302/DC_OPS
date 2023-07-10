from close import Logout
from manage import manage_attendance
from dbconnection import conn,cur
class student():
    def viewdetails(self):
        Stuid=input("\nStudent's ID : ")
        idquery="select * from studentdetails where StuID = %s"
        iddata=(Stuid,)
        cur.execute(idquery,iddata)
        b=cur.fetchone()
        if b:
            print("Student Name : ",b[1])
            print("Student Email : ",b[2])  
            print("Number of days Absent : ",b[3])
            print("Student Attendance : ",b[4]) 
            print("------------------------------------------")
            print("1 - Add student\n2 - View students details\n3 - Manage attendance\n4 - Logout")
            try:
                number=int(input("\nEnter choice : "))
                if(number==1):
                    student.addstudent(self)
                elif(number==2):
                    student.viewdetails(self)
                elif(number==3):
                    manage_attendance.manage(self)
                elif(number==4):
                    Logout.logout(self=None)
                else:
                    print("Enter valid number")
            except ValueError:
                print("Enter an integer")
    def addstudent(self):
        Student_ID=input("\nStudent ID : ")
        Student_name=input("Student name : ")
        Student_Email=input("Student Email : ")
        Student_Leave=int(input("No of leaves : "))
        Student_attendance=int(100-Student_Leave)
        addquery="insert into studentdetails values(%s, %s, %s, %s, %s)"
        addata=(Student_ID,Student_name,Student_Email,Student_Leave,Student_attendance)
        cur.execute(addquery,addata)
        conn.commit()
        print("*---Student added successfully---*")
        print("------------------------------------------")
        print("1 - Add student\n2 - View students details\n3 - Manage attendance\n4 - Logout")
        try:
            number=int(input("Enter choice : "))
            if(number==1):
                student.addstudent(self)
            elif(number==2):
                student.viewdetails(self)
            elif(number==3):
                manage_attendance.manage(self)
            elif(number==4):
                Logout.logout(self=None)
            else:
                print("Enter given number")
        except ValueError:
            print("Enter an integer")