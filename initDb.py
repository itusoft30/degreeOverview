import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
    """
    CREATE TABLE DEPARTMENT ( 
                    Department_ID SERIAL PRIMARY KEY, 
                    Department_Name VARCHAR(50), 
                    Faculty_Name VARCHAR(50)
                    );
    CREATE TABLE REGUSER ( 
                    User_ID SERIAL PRIMARY KEY, 
                    Name VARCHAR(30), 
                    Surname VARCHAR(30),
                    Email VARCHAR(50) UNIQUE NOT NULL,
                    Password VARCHAR(100) NOT NULL,
                    Department_ID INTEGER REFERENCES DEPARTMENT (Department_ID),
                    User_type INTEGER DEFAULT 0
                    );
    CREATE TABLE INSTRUCTOR ( 
                    Instructor_ID INTEGER REFERENCES REGUSER (User_ID) UNIQUE, 
                    Title VARCHAR(50)
                    );
    CREATE TABLE STUDENT ( 
                    Student_ID INTEGER REFERENCES REGUSER (User_ID) UNIQUE,
                    Id_Number VARCHAR(9) 
                    );
    CREATE TABLE COURSE ( 
                    Course_ID SERIAL PRIMARY KEY, 
                    Crn VARCHAR(5),
                    Name VARCHAR(50),
                    Course_Code VARCHAR(10),
                    Instructor_ID INTEGER REFERENCES INSTRUCTOR (Instructor_ID),
                    Credit INTEGER,
                    Department_ID INTEGER REFERENCES DEPARTMENT (Department_ID)
                    );
    CREATE TABLE OUTCOME (
                    Outcome_ID SERIAL PRIMARY KEY,
                    Name VARCHAR(30)
                    );
    CREATE TABLE COURSE_OUTCOME (
                    Course_Outcome_ID SERIAL PRIMARY KEY,
                    Course_ID INTEGER REFERENCES COURSE (Course_ID),
                    Outcome_ID INTEGER REFERENCES OUTCOME (Outcome_ID)
                    );
    CREATE TABLE PREREQUISITE (
                    Prerequisite_ID SERIAL PRIMARY KEY,
                    Course_ID INTEGER REFERENCES COURSE (Course_ID),
                    Requisite_ID INTEGER REFERENCES COURSE (Course_ID)
                    );
    CREATE TABLE STUDENT_GRADE (
                    Student_Grade_ID SERIAL PRIMARY KEY,
                    Student_ID INTEGER REFERENCES STUDENT (Student_ID),
                    Course_ID INTEGER REFERENCES COURSE (Course_ID),
                    Grade VARCHAR(2)
                    );
       
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Computer Engineering', 'Faculty of Computer and Informatics Engineering');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Civil Engineering', 'Faculty of Civil Engineering');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Geomatics Engineering', 'Faculty of Civil Engineering');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Enviromental Engineering', 'Faculty of Civil Engineering');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Architecture', 'Faculty of Architecture');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Urban and Regional Planning', 'Faculty of Architecture');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Interior Architecture', 'Faculty of Architecture');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Landscape Architecture', 'Faculty of Architecture');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Electronics & Communication Engineering', 'Faculty of Electrical and Electronic Engineering');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Electrical Engineering', 'Faculty of Electrical and Electronic Engineering');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Electronics Engineering', 'Faculty of Electrical and Electronic Engineering');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Communication Engineering', 'Faculty of Electrical and Electronic Engineering');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Control and Automation Engineering', 'Faculty of Electrical and Electronic Engineering');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Mechanical Engineering', 'Faculty of Mechanical Engineering');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Manufacturing Engineering', 'Faculty of Mechanical Engineering');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Management Engineering', 'Faculty of Management');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Industrial Engineering', 'Faculty of Management');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Economy', 'Faculty of Management');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Mathematics Engineering', 'Faculty of Science and Letters');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Physics Engineering', 'Faculty of Science and Letters');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Chemistry', 'Faculty of Science and Letters');
    INSERT INTO DEPARTMENT (Department_Name, Faculty_Name) 
    VALUES ('Molecular Biology and Genetics', 'Faculty of Science and Letters');
    
    INSERT INTO REGUSER (Name, Surname, Email, Password, User_type) 
    VALUES ('admin','admin','admin@gmail.com', 'gAAAAABd9BaEELg95qbxr7i1H-bnoUGyjGnEBYjAnVOpXEZFvwCdUoDzPuIgny3W1ou9JwwiR-WeIv0YgPU21OKI7T2Tg5wgCA==', 0);
    INSERT INTO REGUSER (Name, Surname, Email, Password, Department_ID, User_type) 
    VALUES ('Iskender','Akyuz','akyuzi15@itu.edu.tr', 'gAAAAABd9BaEELg95qbxr7i1H-bnoUGyjGnEBYjAnVOpXEZFvwCdUoDzPuIgny3W1ou9JwwiR-WeIv0YgPU21OKI7T2Tg5wgCA==', (select Department_ID from DEPARTMENT where DEPARTMENT.Department_Name='Computer Engineering'), 2);
    INSERT INTO STUDENT (Student_ID, Id_Number) 
    VALUES ((select User_ID from REGUSER where REGUSER.Email='akyuzi15@itu.edu.tr'),'150150150');
    INSERT INTO REGUSER (Name, Surname, Email, Password, Department_ID, User_type) 
    VALUES ('Nurdogan','Karaman','karamann15@itu.edu.tr', 'gAAAAABd9BaEELg95qbxr7i1H-bnoUGyjGnEBYjAnVOpXEZFvwCdUoDzPuIgny3W1ou9JwwiR-WeIv0YgPU21OKI7T2Tg5wgCA==', (select Department_ID from DEPARTMENT where DEPARTMENT.Department_Name='Computer Engineering'), 2);
    INSERT INTO STUDENT (Student_ID, Id_Number) 
    VALUES ((select User_ID from REGUSER where REGUSER.Email='karamann15@itu.edu.tr'),'150150141');
    
    INSERT INTO REGUSER (Name, Surname, Email, Password, Department_ID, User_type) 
    VALUES ('Hayri Turgut', 'Uyar','uyar@itu.edu.tr', 'gAAAAABd9BaEELg95qbxr7i1H-bnoUGyjGnEBYjAnVOpXEZFvwCdUoDzPuIgny3W1ou9JwwiR-WeIv0YgPU21OKI7T2Tg5wgCA==', (select Department_ID from DEPARTMENT where DEPARTMENT.Department_Name='Computer Engineering'), 1);
    INSERT INTO INSTRUCTOR (Instructor_ID, Title) 
    VALUES ((select User_ID from REGUSER where REGUSER.Email='uyar@itu.edu.tr'),'Teaching Assistant');
    
    INSERT INTO REGUSER (Name, Surname, Email, Password, Department_ID, User_type) 
    VALUES ('Ayşe', 'Tosun','tosun@itu.edu.tr', 'gAAAAABd9BaEELg95qbxr7i1H-bnoUGyjGnEBYjAnVOpXEZFvwCdUoDzPuIgny3W1ou9JwwiR-WeIv0YgPU21OKI7T2Tg5wgCA==', (select Department_ID from DEPARTMENT where DEPARTMENT.Department_Name='Computer Engineering'), 1);
    INSERT INTO INSTRUCTOR (Instructor_ID, Title) 
    VALUES ((select User_ID from REGUSER where REGUSER.Email='tosun@itu.edu.tr'),'Assistant Professor');
    
    INSERT INTO COURSE (Crn, Name, Course_Code, Instructor_ID, Credit, Department_ID)
    VALUES ('27521', 'Database Systems', 'BLG317E', (select User_ID from REGUSER where REGUSER.Email='uyar@itu.edu.tr'), 3, (select Department_ID from DEPARTMENT where DEPARTMENT.Department_Name='Computer Engineering'));
    
    INSERT INTO COURSE (Crn, Name, Course_Code, Instructor_ID, Credit, Department_ID)
    VALUES ('25236', 'Introduction to C', 'BLG105E', (select User_ID from REGUSER where REGUSER.Email='tosun@itu.edu.tr'), 3, (select Department_ID from DEPARTMENT where DEPARTMENT.Department_Name='Computer Engineering'));
    
    INSERT INTO OUTCOME (Name) VALUES ('C Programming');
    INSERT INTO OUTCOME (Name) VALUES ('SQL');
    INSERT INTO OUTCOME (Name) VALUES ('Basic Programming');
    INSERT INTO OUTCOME (Name) VALUES ('Algorithm');
    
    INSERT INTO COURSE_OUTCOME (Course_ID, Outcome_ID) VALUES ((select Course_ID from COURSE where COURSE.Name='Introduction to C'), (select Outcome_ID from OUTCOME where Outcome.Name='C Programming'));
    INSERT INTO COURSE_OUTCOME (Course_ID, Outcome_ID) VALUES ((select Course_ID from COURSE where COURSE.Name='Introduction to C'), (select Outcome_ID from OUTCOME where Outcome.Name='Algorithm'));
    INSERT INTO COURSE_OUTCOME (Course_ID, Outcome_ID) VALUES ((select Course_ID from COURSE where COURSE.Name='Database Systems'), (select Outcome_ID from OUTCOME where Outcome.Name='SQL'));
    
    INSERT INTO PREREQUISITE (Course_ID, Requisite_ID) VALUES ((select Course_ID from COURSE where COURSE.Name='Database Systems'), (select Course_ID from COURSE where COURSE.Name='Introduction to C'));
    
    INSERT INTO STUDENT_GRADE (Student_ID, Course_ID, Grade) VALUES ((select Student_ID from STUDENT where STUDENT.Student_ID=3), (select Course_ID from COURSE where COURSE.Name='Database Systems'), 'VF');
    """
]


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
