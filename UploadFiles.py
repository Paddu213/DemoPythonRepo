import pyodbc

server = 'HCL-02-24\SQLEXPRESS'
database = 'SearchEngine'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

#To upload and receive SearchEngine,class UploadFilesToDB connects to a SQl database
class Updating_DB:
    #To display all the SerachEngine that are saved in our database table,we use the method show_file_search_results_fromdb
    def show_file_search_results_fromdb(self):
        values = cursor.execute('select * from SearchEngine_Table')
        for fileInfo in values:
            print("File Name: {}".format(fileInfo.NameOfFile))
            print("File Location: {}".format(fileInfo.File_Location))
    #Our database table inputs are uploaded as SearchEngine using the upload file results todb method.
    #it takes inputs as file name,filelocation and searchcount for newly searched files.
    def upload_file_results_todb(self,fileName, fileLocation, searchCount):
        #Create an insert query to commit the results of SearchEngine to a db table.
        query = '''  
                    INSERT INTO SearchEngine_Table (File_Location, SearchCount, NameOfFile)
                    VALUES
                    ('{0}',{1},'{2}')  '''

        insertQuery = query.format(fileLocation, searchCount, fileName)
        cursor.execute(insertQuery)
        cnxn.commit()
        print("New file search results committed to DB")

    # Takes a filename as input and searches in the database for that file.
    # Input : Filename (string)
    # output : True or False (Boolean)
    def search_in_db_for_file(self, fileName):
        # Choose a query using the filter"filename".
        query = ''' select * from SearchEngine_Table where NameOfFile = '{0}' '''
        searchQuery = query.format(fileName)
        values = cursor.execute(searchQuery)
        print("File search results from DB.")
        flag=1

        for fileInfo in values:
            #print("==========================")
            print("File name: {} - File path: {} ".format(fileInfo.NameOfFile, fileInfo.File_Location))
            flag=0

        if flag == 0:
            self.update_file_searchcount(fileName)
            return False
        else:
            return True


    #update file searchcount method is used to update a file search count.The most serached files are determined using searchcount.
    def update_file_searchcount(self, fileName):
        try:
            query = ''' select * from SearchEngine_Table where NameOfFile = '{0}' '''
            searchQuery = query.format(fileName)
            values = cursor.execute(searchQuery)
            for fileInfo in values:
                fileSearchCount = fileInfo.SearchCount
                #Building an update query to add a single file search.
                fileinfoQuery = '''
                        Update SearchEngine_Table SET SearchCount = {0} WHERE NameOfFile = '{1}'
                        '''
                updateQuery = fileinfoQuery.format(fileSearchCount + 1, fileName)
                cursor.execute(updateQuery)
                #commits data to DB
                cursor.commit()
                print("Updated file search count")

        except:
            pass