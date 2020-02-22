import os
from os import path

def Menu():
    print('''Select the option:
    1 - Work with file
    2 - Work with directory
    0 - Exit''')


def work_file():
    print('''Select the option:
    0 - Create new file
    1 - Delete file
    2 - Rename file
    3 - Add content to this file
    4 - Rewrite content of this file
    5 - Return to the parent directory
    6 - Menu''')
    cmnd=int(input("Command:"))

    if(cmnd==1):
        my_file=raw_input('Name of file to delete:')
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), my_file)
        os.remove(path)
        work_file()
    elif(cmnd==0):
        my_file=raw_input('Name of file to create:')
        f=open(my_file,'w')
        f.close()
        print("File created")
        work_file()
        
    elif(cmnd==2):
        src=raw_input("Name of file to rename:")
        dst=raw_input("Enter new name of file:")
        if os.path.exists(src):
            os.rename(src,dst)
            print("File is renamed")
        else:
            print("Error,file is not found")
        work_file()
    elif(cmnd==3):
        my_file=raw_input("Name of file which you want to add content:")
        if os.path.exists(my_file):
            with open(my_file,'w') as f:
                print("You can write new content:")
                content=raw_input("")
                f.write(content)
        else:
            print("Error,file is not found")
        work_file()
    elif(cmnd==4):
        my_file=raw_input("Name of file which you want rewrite:")
        if os.path.exists(my_file):
            with open(my_file,'w') as f:
                print("You can rewritecontent:")
                content=raw_input()
                f.write(content)
        else:
            print("Error,file is not found")
        work_file()
    elif(cmnd==5):
        work_directory()
    elif(cmnd==6):
        Menu()

        
def work_directory():
    print('''Select the option:
    0 - Create directory
    1 - Rename directory
    2 - Print number of files in it
    3 - Print number of directories in it
    4 - List content of the directory 
    5 - Add file to this directory
    6 - Add new directory to this directory
    7 - Get current directory
    8 - Menu''')
    cmnd=int(input("Command:"))
    if(cmnd==1):
        src=raw_input("Name of directory to rename:")
        dst=raw_input("Enter new name of directory:")
        if os.path.exists(src):
            os.rename(src,dst)
            print("Directory is renamed")
        else:
            print("Error,directory is not found")
        work_directory()
    elif(cmnd==0):
        src=raw_input("Name of directory to create:")
        os.mkdir(src)
        work_directory()
    
    elif(cmnd==2):
        cnt=0
        dir=raw_input("Enter the directory:")
        for path in os.listdir(dir):
            if os.path.isfile(os.path.join(dir,path)):
                cnt+=1
        print cnt
        work_directory()
    elif(cmnd==3):
        cnt=0
        dir=raw_input("Enter the directory:")
        for path in os.listdir(dir):
            if os.path.isdir(os.path.join(dir,path)):
                cnt+=1
        print cnt
        work_directory()
    elif(cmnd==4):
        dir=raw_input("Enter the directory:")
        print(os.listdir(dir))
        work_directory()
    elif(cmnd==5):
        dir=raw_input("Enter the directory:")
        name =raw_input("Enter new file's name: ")
        file = open(os.path.join(dir, name), mode = "w")
        print("File created")
        file.close()
        work_directory()
    elif(cmnd==6):
        dir=raw_input("Enter the directory:")
        name = raw_input("Enter the new directory's name: ")
        folder = os.mkdir(dir + "//" + name)
        print("Directory created")
        work_directory()
    elif(cmnd==7):
        print(os.getcwd())
        work_directory()
    elif(cmnd==8):
        Menu()

    
Menu()
option=int(input('Option:'))
if(option==1):
    work_file()
elif(option==2):
    work_directory()
elif(option==0):
    print("Goodbye!!!")
