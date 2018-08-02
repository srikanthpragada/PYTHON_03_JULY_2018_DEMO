import sqlite3

con = sqlite3.connect(r"e:\classroom\python\july3\hr.db")     # Connection
cur = con.cursor()                                            # Cursor

cur.execute("select * from departments order by deptid ")
for row in cur.fetchall():
    print(row[0], row[1], row[2])




