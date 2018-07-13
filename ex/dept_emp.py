depts = {}

while True:
    deptno = int(input("Enter department no. :"))
    if deptno == 0:
        break

    empname = input("Enter employee name : ")
    if deptno in depts:
        depts[deptno].append(empname)
    else:
        depts[deptno] = [empname]

for dn, enames in depts.items():
    print(dn, ",".join(enames))
