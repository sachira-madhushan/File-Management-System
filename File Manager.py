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
	print("\t[1]-List files and folders")
	print("\t[2]-Create folder")
	print("\t[3]-Change location")
	print("\t[4]-Rename folder")
	print("\t[5]-Delete folder")
	print("\t[6]-Create file")
	print("\t[7]-Rename file")
	print("\t[8]-Delete file")
	print("\t[9]-Write file")
	print()
	x=int(input("[?]Select your option :"))
	if x==1:
		listDir()
	if x==2:
		createDir()
	if x==3:
		changeLocation()


def listDir():
	os.system("cls")
	print("================================================")
	print("================Files and folders===============")
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

def createDir():
	os.system("cls")
	print("================================================")
	print("==================Create Folder=================")
	print("================================================")
	print("================================================")
	print()
	print()
	dname=input("[?]folder name :")
	if os.path.exists(os.path.join(os.getcwd(),dname)):
		os.system("cls")
		print("[Failed]Folder already exists!")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		createDir()
	else:
		os.system("mkdir "+dname)
		os.system("cls")
		print("[Done]Folder created!")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		logo()
		options()

def changeLocation():
	os.system("cls")
	print("================================================")
	print("=================Change Location================")
	print("================================================")
	print("================================================")
	print()
	print()
	os.system("echo [Current location] %cd%")
	print()
	print("[>]Folder List")
	os.system("dir /ad")
	print()
	print("[>]Tips")
	print("\t[*]To go back use two dots")
	print("\t[*]If you done changing location type done")
	print()
	x=input("[?]Folder name to go :")
	if x=="..":
		os.system("cd ..")
		changeLocation()
	if os.path.exists(os.path.join(os.getcwd(),x):
		os.system("cd "+x)
		changeLocation()
	else:
		print("[Failed]Invalied folder!")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		changeLocation()

logo()
options()
os.system("pause")