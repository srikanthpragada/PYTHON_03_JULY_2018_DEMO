CREATE TABLE departments (
    deptid   INTEGER   PRIMARY KEY AUTOINCREMENT,
    deptname TEXT (30) NOT NULL,
    location text (30)
);

insert into departments(deptname,location) values('IT','Bangalore')
insert into departments(deptname,location) values('SALES','Mumbai')
