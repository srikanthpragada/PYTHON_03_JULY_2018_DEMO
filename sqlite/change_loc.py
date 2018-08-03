import sqlite3

con = sqlite3.connect(r"e:\classroom\python\july3\hr.db")     # Connection
cur = con.cursor()                                            # Cursor

id = input("Enter department id :")
loc = input("Enter new location :")

cur.execute("update departments set location = ? where deptid = ?", (loc,id))
if cur.rowcount == 1:
    print("Successfully updated!")
    con.commit()
else:
    print("Department Id Not Found!")







