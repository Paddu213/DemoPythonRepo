import pyodbc
server='HCL-02-24\SQLEXPRESS'
database='FileSearchResults'
username='capstone'
password='Capstone@123'

cnxn=pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
