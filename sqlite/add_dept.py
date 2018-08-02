import sqlite3

con = sqlite3.connect(r"e:\classroom\python\july3\hr.db")     # Connection
cur = con.cursor()                                            # Cursor

name = input("Enter department name :")
loc = input("Enter department location :")

cur.execute("insert into departments(deptname,location) values(?,?)", (name,loc))
con.commit()






