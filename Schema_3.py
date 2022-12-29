import pyodbc

server = 'HCL-02-24\SQLEXPRESS'
database = 'SearchEngine'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


class AlreadyExists(Exception):
    pass


class Employee_schema:
    def Employee_Info_table(self):
        try:
            #values = cursor.execute('''select * from Employee_details''')
            #if (not (values)):
            query_2 = cursor.execute('''use SearchEngine''')
            query_3 = cursor.execute('''create table Employee_Info
                                    (
                                    Name varchar(50),
                                    Salary int,
                                    Project varchar(50),
                                    Emp_Id int NOT NULL,
                                    primary key(Emp_Id)
                                    )
                                     ''')
            query_4 = cursor.execute('''select * from Employee_Info''')
            cnxn.commit()
            #else:
                #raise AlreadyExists
        except AlreadyExists:
            print("Table already exists in DB")
#obj=Employee_schema()
#obj.Employee_Info_table()

