import os
import concurrent.futures
import time
import win32api
start=time.perf_counter()

availableDrive=win32api.GetLogicalDriveStrings()
#print(availableDrive)
Drives=[drivestr for drivestr in availableDrive.split('\000') if drivestr]

#drives=drives.split('\000')[:-1]

def find_files(filename, search_path):
    result = []
    # Waking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result

input_file='Text document.txt'
with concurrent.futures.ThreadPoolExecutor() as executor:
    results=[executor.submit(find_files,input_file,drive) for drive in Drives]
    print(results)
    for r in concurrent.futures.as_completed(results):
        print(r.result())


finish=time.perf_counter()
print(f"time {finish-start} seconds")

