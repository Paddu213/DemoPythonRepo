import os    #To interact with the under lying Operating System.
import time  #Here to calculate the time taken by the process.
import win32api                          #To Get the all the drives in our system.
start=time.perf_counter()                #To start the timer.
def find_files(filename, search_path):
    result = []
    # for loop is used to search the files by walking through all the folders of drive
    for root, dir, files in os.walk(search_path):
        # To chech whether the filename matches the files or not
        if filename in files:
            result.append(os.path.join(root, filename)) #filename and root will be appended to result list
    return result
#to get all the drives available in our system
for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
    # here iam calling the method called find_files it walks through the all drive and displays that file particular path
    print(find_files("Text document.txt", drive))
finish=time.perf_counter()
print(f"time {finish-start} seconds")