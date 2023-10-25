import asyncio
import os

def get_typ( filename, dire):
    file_split = os.path.splitext(filename)
    print(file_split)
    file_extension = file_split[1]
    print("File Name: ", filename)
    print("File Extension: ", file_extension)
    if file_extension == ".pdf":
        new_dir = "PDF\\"
        new_path=os.path.join(dire,new_dir)
        try: 
            os.makedirs(new_path, exist_ok = True) 
            print("Directory '%s' created successfully" % new_dir) 
        except OSError as error: 
            print("Directory '%s' can not be created" % new_dir) 
        os.rename(dire, new_path + filename)
    elif file_extension == ".jpeg":
        new_dir = "jpeg\\"
        new_path=os.path.join(dire,new_dir)
        try: 
            os.makedirs(new_path, exist_ok = True) 
            print("Directory '%s' created successfully" % new_dir) 
        except OSError as error: 
            print("Directory '%s' can not be created" % new_dir) 
        os.rename(dire, new_path + filename)
    elif file_extension == ".zip":
        new_dir = "ZIP\\"
        new_path=os.path.join(dire,new_dir)
        try: 
            os.makedirs(new_path, exist_ok = True) 
            print("Directory '%s' created successfully" % new_dir) 
        except OSError as error: 
            print("Directory '%s' can not be created" % new_dir) 
        os.rename(dire, new_path + filename)


    

def find_files(direc):
    b = os.scandir(direc)
    print("Files in '%s' " % direc)
    for files in b :
        if files.is_dir() or files.is_file():
            if files.is_file():
                get_typ(files.name, direc)
            print(files.name)
    


print("Hello, Script will begin please give me the directory to your download folder :D.")

direc = input()

print("finding files ...")
find_files(direc)
