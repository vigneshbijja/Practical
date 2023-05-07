-- DDL--


CREATE TABLE Students
(
 
    Roll_no INT PRIMARY KEY,
    Name VARCHAR(20),
    Age INT,
    Address VARCHAR(30)
);

ALTER TABLE Students ADD Date_Of_Birth  DATE;

TRUNCATE TABLE Students;

DROP TABLE Students;


















-- DML --

CREATE TABLE Students (
  Roll_no INT PRIMARY KEY,
  Name VARCHAR(50),
  Age INT,
  Address VARCHAR(100),
  Date_of_Birth DATE
);

INSERT INTO Students (Roll_no,Name,Age,Address,Date_of_Birth) VALUES (1, 'John', 16, 'Pune', '2006/06/06');

INSERT INTO Students (Roll_no,Name,Age,Address,Date_of_Birth) VALUES (2, 'Ajay', 15, 'Chennai', '2007/10/02');

INSERT INTO Students (Roll_no,Name,Age,Address,Date_of_Birth) VALUES (3, 'Ron', 12, 'Delhi', '2010/08/31');

INSERT INTO Students (Roll_no,Name,Age,Address,Date_of_Birth) VALUES (4, 'Joy', 16, 'Mumbai', '2006/01/01');

INSERT INTO Students (Roll_no,Name,Age,Address,Date_of_Birth) VALUES (5, 'Harry', 15, 'Hyderabad', '2007/12/31');


SELECT * FROM Students;

UPDATE Students
SET Address= 'Nashik'
WHERE Address= 'Pune';


DELETE FROM Students WHERE Roll_no = 2;


SELECT * FROM Students;
























-- DQL --

CREATE TABLE my_table(
    first_name varchar(20),
    age INT
);


alter table my_table
add column employed boolean;


rename table my_table to some_table;


truncate table some_table;
