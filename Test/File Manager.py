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