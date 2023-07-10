from dbconnection import conn,cur
Rollno=input("Enter Rollno : ")
days=int(input("Enter no.of.days : "))
Reason=input("Enter reason : ")
cur.execute("insert into leavedetails values(%s,%s,%s,'\0')",(Rollno,days,Reason))
conn.commit()
choice=input("Do you need to view the decision? ")
if choice == "yes":
    ID=input("Enter Rollno : ")
    cur.execute("select * from leavedetails where StuID = %s",(ID,))
    for i in cur:
        print(i)
else:
    print("Thankyou")