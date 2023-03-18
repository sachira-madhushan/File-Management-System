import os

#system window settings 
os.system("mode con:cols=50 lines=30");
os.system("title=File Management System v1.0")
os.system("color 02")
#system window settings end

def logo():
	os.system("cls")
	print("================================================")
	print("===========File Management System v1.0==========")
	print("================================================")
	print("================================================")
	os.system("color 05")
	os.system("timeout 01>>nul")
	os.system("color 03")
	os.system("timeout 01>>nul")
	os.system("color 02")
	os.system("echo [Current location] %cd%")
	print()


def options():
	print("[v1.0]Let's see what we can do:")
	print("\t[1]-List directories")
	print("\t[2]-Create directory")
	print("\t[3]-Change directory")
	print("\t[4]-Rename directory")
	print("\t[5]-Delete directory")
	print("\t[6]-Create file")
	print("\t[7]-Rename file")
	print("\t[8]-Delete file")
	print("\t[9]-Write file")
	print()
	x=int(input("[?]Select your option :"))


def listDir():
	os.system("cls")
	print("================================================")
	print("===================Directories==================")
	print("================================================")
	print("================================================")
	print()
	print()
	os.system("dir")
	print()
	print("[!]Press any key to go back.")
	os.system("pause>>nul")
	logo()
	options()

logo()
options()
os.system("pause")