import os
import shutil
import time, datetime
from zipfile import ZipFile
#Defined path
path = "/Users/samuelvarghese/Documents"

#Getting list of files in a directory
list_of_files = os.listdir(path)
#Getting year
year = datetime.datetime.now()
year = int(year.year)
#List of files to be zipped 
to_zip_list = []

#ZipFile with 'w' initiated
zip_file_path = path+"/"+'Test1.zip'
zip_create = ZipFile(zip_file_path, 'w')

#Iterate through all the files in the list
for file_ in list_of_files:
    name, ext = os.path.splitext(file_)
    ext = ext[1:]

    #Indicates directory, if so countinue on to the next
    if ext == " ":
        continue
    #time.ctime is needed to convert to human readable time lol
    date = time.ctime(os.path.getmtime(path+"/"+file_))
    #print(date)

    #Get the last element of the split which contains the year
    year_of_file = date.split()[-1]
    #print(year_of_file)
    #convert to int
    year_of_file = int(year_of_file) # convert to int to subtract
    if year - year_of_file == 2:
        # if os.path.exists(path+"/"+(str(year_of_file))) == False:
        #     os.mkdir(path+"/"+(str(year_of_file)))
        to_zip_list.append(file_)
        print("Files to zip: ", str(file_))

    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file_, path+"/"+ext+"/"+file_)
    else:
        os.mkdir()
    #work on sorter

for files in to_zip_list:
    if str(files)[0] == '.':
        continue
    #first arugement takes the file path, second arugment is for the directory in zip file
    zip_create.write(path+"/"+files, files)