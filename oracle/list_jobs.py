import os
import cx_Oracle

# Set folder in which Instant Client is installed in system path
os.environ['PATH'] = r'c:\oraclexe\instantclient_12_2'

# Connect to hr account in Oracle Database 11g Express Edition
con = cx_Oracle.connect("hr", "hr", "localhost/xe")
cur = con.cursor()
cur.execute("select * from jobs")
for job in cur.fetchall():
    print(job[1])

con.close()



