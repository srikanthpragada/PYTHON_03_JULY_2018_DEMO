import sqlite3

con = sqlite3.connect(r"e:\classroom\python\july3\hr.db")     # Connection
cur = con.cursor()                                            # Cursor

id = input("Enter department id :")

cur.execute("delete from departments where deptid = ?", (id,))
if cur.rowcount == 1:
    print("Successfully Deleted!")
    con.commit()
else:
    print("Department Id Not Found!")







