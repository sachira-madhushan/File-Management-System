import os
#system window settings

os.system("mode con:cols=50 lines=30");
os.system("title=File Management System v1.0")
os.system("color 02")
#system window settings end


def rename():
    print("================================================")
    print("==================Rename Folder=================")
    print("================================================")
    print("================================================")

    oldname = input("enter folder name that you want rename ?")
    newname = input("enter new folder name to that you want to rename?")
    os.system("ren " + oldname + " " + newname)

def delete_folder():
    print("================================================")
    print("==================Delete Folder=================")
    print("================================================")
    print("================================================")

    del_filename = input ("enter name that you want to delete :")
    os.system("rmdir "+del_filename)

def create_file() :
    print("================================================")
    print("==================Create File===================")
    print("================================================")
    print("================================================")

    filename = input("enter file name that you want to create (plase enter name with extention) :")
    os.system("echo >  " + filename)

def rename_file():
    print("================================================")
    print("==================Rename File===================")
    print("================================================")
    print("================================================")

    oldname = input("enter file name with extention that you want rename ?")
    newname = input("enter new file name with extention to that you want to rename?")
    os.system("ren " + oldname + " " + newname)

def delete_file():
    print("================================================")
    print("==================Delete File===================")
    print("================================================")
    print("================================================")

    del_name = input("enter file name with extention do you want to delete :")
    os.system("del " +del_name)

def write_file():
    print("================================================")
    print("==================Write File====================")
    print("================================================")
    print("================================================")

    input_line = input("enter that you want to wite in your :")
    file_name = input("enter file name with extention to input that content:")
    os.system("echo " +input_line+" > "+file_name)