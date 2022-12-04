#Python Count Number of Files in a Directory.
#Count Number Files in a directory.
import os
#folder path
dir_path = 'D:\Python_Winter_2022_3'
count = 0
#Iterate directory
for path in os.listdir(dir_path):
    #check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('File count:', count)
print(os.path.join(dir_path, path))
print(os.listdir(os.path.join(dir_path, path)))
#Another way:
#Count all files in the directory and its subdirectories
import os
count = 0
for root_dir, cur_dir, files in os.walk(r'D:\Python_Winter_2022_3'):
    count += len(files)
print('file count:', count)
#Another way:
#scandir() to count all files in the directory.
import os
count = 0
dir_path = 'D:\Python_Winter_2022_3'
for path in os.scandir(dir_path):
    if path.is_file():
        count += 1
print('file count:', count)
#fnmatch module to count all files in the directory.
#The fnmatch supports pattern matching, and it is faster.
#For example, we can use fnmatch to find files that match the pattern *.* The * is a wildcard which means any name. So *.* indicates any file name with any extension, nothing but all files.
#Next, we will use the filter() method to separate files returned by the listdir() function using the above pattern
#In the end, we will count files using the len() function.
import fnmatch
dir_path = 'D:\Python_Winter_2022_3'
count = len(fnmatch.filter(os.listdir(dir_path), '*.*'))
print('File Count:', count)