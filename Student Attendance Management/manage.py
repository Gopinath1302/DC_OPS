from close import Logout
from dbconnection import conn,cur
class manage_attendance():
    def manage(self):
        viewleaves=input("Do you need to view the leaves applied by the students? ")
        if viewleaves=="yes":
            cur.execute("select * from leavedetails where Approve_or_Cancel='\0'")
            for i in cur:
                print(i)
                res=input("Approve/Cancel : ")
                if res=="Approved":
                    cur.execute("update leavedetails set Approve_or_Cancel = %s",(res,))
                    cur.execute("update studentdetails set no_of_leaves= no_of_leaves+%s,Attendance = Attendance-%s where StuID = %s",(i[1],i[1],i[0]))
                    conn.commit()
                if res=="Canceled":
                    cur.execute("update leavedetails set Approve_or_Cancel = %s",(res,))
                    conn.commit()
            else:
                print("No leave updates yet")
        print("")
        print("------------------------------------------")
        print("")
        res=input("Do you want to exit : ")
        if res=="yes":
            Logout.logout(self)
        else:
            manage_attendance.manage(self)

