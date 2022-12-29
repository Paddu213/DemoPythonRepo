import pyodbc

server = 'HCL-02-24\SQLEXPRESS'
database = 'Python_Project'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class AlreadyExists(Exception):
    pass
class Employee_schema:
    def Employee_table(self):
        try:
            values = cursor.execute('''select * from Employee_details''')
            if (not (values)):
                query_1=cursor.execute('''create database Python_Project''')
                query_2 = cursor.execute('''use Python_Project''')
                query_3 = cursor.execute('''create table Employee_details
                                    (
                                    Name varchar(50),
                                    Salary int,
                                    Project varchar(50)
                                    )
                                     ''')
                query_4 = cursor.execute('''select * from Employee_details''')
                cnxn.commit()
            else:
                raise AlreadyExists
        except AlreadyExists:
            print("Table already exists in DB")
