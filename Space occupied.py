#Question: Please write a program that for a given folder i.e. (my_folder = r'c:\users') counts all files in it and
#its subfolders (including their subfolders) and then also computes the total space occupied by all those files.
import os #The os module provides many functions for interacting with the operating system.
def File_count(Dir_path):
  Count = 0 #This counter variable contains how many files are present in a directory.
  for Files_list in os.listdir(Dir_path): #The os.listdir('path') function returns a list of files and directories present in the given directory.
    #print(os.listdir(dir_path))
    File = (os.path.join(Dir_path, Files_list))
    #print(file)
    if os.path.isfile(File): #Checking whether the current entry is a file or directory.
      Count += 1 #If it is a file, increment the counter by 1.
    elif os.path.isdir(File):
      Count +=File_count(File)
  return Count
Count = File_count('D:\Python_Winter_2022_3') #Looking files for counting.
print("Count all files: " + str(File_count("."))) #"." meaning Current folder.
def Folder_size(Folder):
  Total_size = 0 #Provides the size in bytes.
  for Files in os.listdir(Folder):
    File_path = os.path.join(Folder, Files)
    if os.path.isfile(File_path):
      Total_size += os.path.getsize(File_path)
    elif os.path.isdir(File_path):
      Total_size += Folder_size(File_path)
  return Total_size
Folder = Folder_size('D:\Python_Winter_2022_3')
print("Total space(size): " + str(Folder_size(".")))

