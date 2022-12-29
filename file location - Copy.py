import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'HCL-02-24\SQLEXPRESS'
database = 'FileSearchResults1'
username = 'capstone'
password = 'Capstone@123'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

print(cnxn)
cursor = cnxn.cursor()
print(cursor)

cursor.execute('''
                INSERT INTO FileSearchResults1_table (File_Location, SearchCount, NameOfFile)
                VALUES
                ('F:\a',1,'Text document'),
                ('F:\mainfile(1)\sub_1\apple\dairy_milk\boost\sweet',3,'Text document')
                 ''')
cnxn.commit()

values=cursor.execute('select * from FileSearchResults1_table')
for i in values:
    print(i)