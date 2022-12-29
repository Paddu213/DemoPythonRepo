import pyodbc

import Schema_3

server = 'HCL-02-24\SQLEXPRESS'
database = 'SearchEngine'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class Existing(Exception):
    pass
class Not_in_Range(Exception):
    pass
class Employees_data:
    Bonus=2
    Projects=['Python','C','Java']
    def __init__(self,Name,Salary,Project,Emp_Id):
        self.Name=Name
        self.Salary=Salary
        self.Project=Project
        self.Emp_Id=Emp_Id
    def insert_values_in_table(self):
        query = '''  
                            INSERT INTO Employee_Info (Name, Salary, Project, Emp_Id)
                            VALUES
                            ('{0}',{1},'{2}','{3}')  '''

        insertQuery = query.format(self.Name, self.Salary, self.Project, self.Emp_Id)
        cursor.execute(insertQuery)


        cnxn.commit()
    def Update_Salary(self,New_Salary,Emp_Id):
        try:
            self.New_Salary = New_Salary
            self.Emp_Id=Emp_Id
            if self.New_Salary != self.Salary:
                fileinfoQuery = '''
                                                Update Employee_Info SET Salary ='{0}' WHERE Emp_Id = '{1}'
                                                '''
                updateQuery = fileinfoQuery.format(New_Salary,Emp_Id)
                cursor.execute(updateQuery)
                cursor.commit()
            else:
                raise Existing
        except Existing:
            print("No Change in Salary")
    def Add_Bonus(self,bonus):
        self.bonus=bonus
        #self.Emp_Id=Emp_Id
        try:
            if self.bonus not in range(1,self.Bonus+1):
                raise Not_in_Range
            else:
                self.Salary=self.Salary+self.Salary*self.bonus
                Query = '''
                        Update Employee_Info SET Salary ='{0}' WHERE Emp_Id = '{1}'
                                                                '''
                updateQuery = Query.format(self.Salary, self.Emp_Id)
                cursor.execute(updateQuery)
                cursor.commit()
        except Not_in_Range:
            print("Bonus is Not in Range")
    def Change_Project(self,project,Emp_Id):
        self.project=project
        self.Emp_Id=Emp_Id

        if self.project in self.Projects:
            if self.project == self.Project:
                print("Project is Already exists")
            else:
                Query = ''' Update Employee_Info SET Project ='{0}' WHERE Emp_Id = '{1}' '''
                updateQuery = Query.format(project, Emp_Id)
                cursor.execute(updateQuery)
                cursor.commit()
        else:
            print("Project is not in list")
    def Display_details(self):
        query=''' select * from Employee_Info WHERE Emp_Id='{0}' '''
        query1=query.format(self.Emp_Id)
        values=cursor.execute(query1)
        for details in values:
            print("Name:{0}  Salary:{1}  Project:{2}  Emp_Id:{3}".format(details.Name , details.Salary , details.Project , details.Emp_Id))

    def delete_row(self,Emp_Id):
        self.Emp_Id=Emp_Id
        query='''Delete from  Employee_Info Where Emp_Id='{0}' 
        '''
        info=query.format(Emp_Id)
        cursor.execute(info)
        cnxn.commit()

obj1=Employees_data('Praveena',30000,'Python',216)
obj=Schema_3.Employee_schema()
#obj.Employee_Info_table()

#obj1.Add_Bonus(2)
#obj1.insert_values_in_table()
#obj1.Update_Salary(35000,213)
#obj1.Change_Project('Java',211)
#obj1.Display_details()
obj1.delete_row(214)


