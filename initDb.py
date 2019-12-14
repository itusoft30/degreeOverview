import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
    """
    CREATE TABLE DEPARTMENT ( 
                    DepartmentID SERIAL PRIMARY KEY, 
                    DepartmentName VARCHAR(50), 
                    FacultyName VARCHAR(50)
                    );
    CREATE TABLE REGUSER ( 
                    UserID SERIAL PRIMARY KEY, 
                    Name VARCHAR(30), 
                    Surname VARCHAR(30),
                    Email VARCHAR(50) UNIQUE NOT NULL,
                    Password VARCHAR(100) NOT NULL,
                    DepartmentID INTEGER REFERENCES DEPARTMENT (DepartmentID),
                    IsAdmin INTEGER DEFAULT 0
                    );
    CREATE TABLE INSTRUCTOR ( 
                    InstructorID INTEGER REFERENCES REGUSER (UserID), 
                    Title VARCHAR(50)
                    );
    CREATE TABLE STUDENT ( 
                    StudentID INTEGER REFERENCES REGUSER (UserID),
                    IdNumber VARCHAR(9) 
                    );
    CREATE TABLE COURSE ( 
                    CourseID SERIAL PRIMARY KEY, 
                    Crn VARCHAR(5),
                    CourseCode VARCHAR(10),
                    InstructorID INTEGER REFERENCES INSTRUCTOR (InstructorID),
                    Credit INTEGER,
                    DepartmentID INTEGER REFERENCES DEPARTMENT (DepartmentID)
                    );
    CREATE TABLE OUTCOME (
                    OutcomeID SERIAL PRIMARY KEY,
                    Name VARCHAR(30)
                    );
    CREATE TABLE COURSEOUTCOME (
                    CourseID INTEGER REFERENCES COURSE (CourseID),
                    OutcomeID INTEGER REFERENCES OUTCOME (OutcomeID)
                    );
    CREATE TABLE PREREQUISITE (
                    CourseID INTEGER REFERENCES COURSE (CourseID),
                    OutcomeID INTEGER REFERENCES OUTCOME (OutcomeID)
                    );
    CREATE TABLE STUDENTGRADE (
                    StudentID INTEGER REFERENCES STUDENT (StudentID),
                    CourseID INTEGER REFERENCES COURSE (CourseID),
                    Grade VARCHAR(2)
                    );

    INSERT INTO REGUSER (Name, Surname, Email, Password, IsAdmin) 
    VALUES ('admin','admin','admin@gmail.com', 'gAAAAABd9BaEELg95qbxr7i1H-bnoUGyjGnEBYjAnVOpXEZFvwCdUoDzPuIgny3W1ou9JwwiR-WeIv0YgPU21OKI7T2Tg5wgCA==', 1);

    INSERT INTO REGUSER (Name, Surname, Email, Password, IsAdmin) 
    VALUES ('Iskender','Akyuz','akyuzi15@itu.edu.tr', 'gAAAAABd9BaEELg95qbxr7i1H-bnoUGyjGnEBYjAnVOpXEZFvwCdUoDzPuIgny3W1ou9JwwiR-WeIv0YgPU21OKI7T2Tg5wgCA==', 0);

    INSERT INTO STUDENT (StudentID, IdNumber) 
    VALUES ((select UserID from REGUSER where REGUSER.Email='akyuzi15@itu.edu.tr'),"15016000");
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
