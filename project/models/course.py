import psycopg2 as dbapi2

class Course:
    @staticmethod
    def AddCourse(crn, name, courseCode, instructorID, credit, departmentID):
        with dbapi2.connect(url) as connection:
            statement = """INSERT INTO COURSE (Crn, Name, CourseCode, InstructorId, Credit, DepartmentID) VALUES (%s, %s, %s, %d, %d, %d);"""
            cursor.execute(statement, (crn, name, courseCode, instructorId, credit, departmentID))
            cursor.close()

    @staticmethod
    def ModifyCourse(courseID, crn, name, courseCode, instructorID, credit, departmentID):
        with dbapi2.connect(url) as connection:
            statement = """UPDATE COURSE SET (Crn = %s, Name = %s, CourseCode = %s, InstructorID = %d, Credit = %d, DepartmentID = %d) WHERE (CourseID = %d);"""
            cursor.execute(statement, (crn, name, courseCode, instructorId, credit, departmentID, courseID))
            cursor.close()

    @staticmethod
    def DeleteCourse(courseID):
        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            statement = """DELETE FROM COURSE WHERE (CourseID = %d);"""
            cursor.execute(statement, (courseID,))
            cursor.close()