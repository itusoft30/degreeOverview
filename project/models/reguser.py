import psycopg2 as dbapi2

class RegUser:
    @staticmethod
    def AddInstructor(name, surname, email, password, title):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            statement = """INSERT INTO REGUSER (Name, Surname, Email, Password) VALUES (%s, %s, %s, %s);"""
            cursor.execute(statement, (name, surname, email, password))
            statement = """INSERT INTO INSTRUCTOR (InstructorID, Title) VALUES ((Select UserID FROM REGUSER WHERE (REGUSER.Email = %s)), %s);"""
            cursor.execute(statement, (email, title))
            cursor.close()

    @staticmethod
    def AddStudent(name, surname, email, password, studentID):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            statement = """INSERT INTO REGUSER (Name, Surname, Email, Password) VALUES (%s, %s, %s, %s);"""
            cursor.execute(statement, (name, surname, email, password))
            statement = """INSERT INTO INSTRUCTOR (StudentID, IdNumber) VALUES ((Select UserID FROM REGUSER WHERE (REGUSER.Email = %s)), %s);"""
            cursor.execute(statement, (email, studentID))
            cursor.close()

    @staticmethod
    def DeleteInstructor(id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            statement = """DELETE FROM INSTRUCTOR WHERE (UserID = %d);"""
            cursor.execute(statement, (id,))
            statement = """DELETE FROM REGUSER WHERE (UserID = %d);"""
            cursor.execute(statement, (id,))
            cursor.close()

    @staticmethod
    def DeleteStudent(id):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            statement = """DELETE FROM STUDENT WHERE (UserID = %d);"""
            cursor.execute(statement, (id,))
            statement = """DELETE FROM REGUSER WHERE (UserID = %d);"""
            cursor.execute(statement, (id,))
            cursor.close()

    @staticmethod
    def UpdateInstructorInfo(id, name, surname, email, title):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            statement = """UPDATE INSTRUCTOR SET (Title = %s) WHERE (InstructorID = %d);"""
            cursor.execute(statement, (title, id))
            statement = """UPDATE REGUSER SET (Name = %s, Surname = %s, Email = %s) WHERE (UserID = %d);"""
            cursor.execute(statement, (name, surname, email, id))
            cursor.close()

    @staticmethod
    def UpdateStudentInfo(id, name, surname, email, studentNum):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            statement = """UPDATE STUDENT SET (IdNumber = %s) WHERE (StudentID = %d);"""
            cursor.execute(statement, (studentNum, id))
            statement = """UPDATE REGUSER SET (Name = %s, Surname = %s, Email = %s) WHERE (UserID = %d);"""
            cursor.execute(statement, (name, surname, email, id))
            cursor.close()

    @staticmethod
    def UpdatePasswordInfo(id, password):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            statement = """UPDATE REGUSER SET (Password = %s) WHERE (UserID = %d);"""
            cursor.execute(statement, (password, id))
            cursor.close()