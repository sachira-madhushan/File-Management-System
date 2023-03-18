import os

#system window settings 
os.system("mode con:cols=100 lines=30");
os.system("title=File Management System v1.0")
os.system("color 02")
#system window settings end

#logo animation for main page
def logo():
	os.system("cls")
	print("================================================")
	print("===========File Management System v1.0==========")
	print("================================================")
	print("================================================")
	os.system("echo [Current location] %cd%")
	print()
#end of logo animation function


#options function
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
	print("\t[10]-Exit")
	print()
	x=int(input("[?]Select your option :"))
	if x==1:
		listDir()
	if x==2:
		createDir()
	if x==3:
		changeLocation()
	if x==4:
		renameDir()
	if x==5:
		delDir()
	if x==6:
		createFile()
	if x==7:
		renFile()
	if x==8:
		delFile()
	if x==9:
		writeFile()
	if x==10:
		os.system("exit")
	else:
		os.system("cls")
		print()
		print("[!]Invalied option.")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		logo()
		options()
#end of options function


#this function is use to list the directories and files in side the current directory
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
#end of the listDir function


#this function is used to create new directory inside the current directory
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
#end of createDir dunction

#this function is used to change the current location of the therminal
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
		os.chdir("..")
		changeLocation()
	elif x=="done":
		logo()
		options()
	elif os.path.exists(os.path.join(os.getcwd(),x)):
		os.chdir(x)
		os.system("pause")
		changeLocation()
	else:
		os.system("cls")
		print("[Failed]Invalied folder!")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		changeLocation()
#end of changeLocation function


#this function is used to rename a folder
def renameDir():
	os.system("cls")
	print("================================================")
	print("==================Rename Folder=================")
	print("================================================")
	print("================================================")
	print()
	print("[>]Folder List")
	os.system("dir /ad")
	print()
	oldname = input("[?]Folder name that you want rename :")
	newname = input("[?]New folder name :")
	if os.path.exists(os.path.join(os.getcwd(),oldname)) and not(os.path.exists(os.path.join(os.getcwd(),newname))):
		os.system("ren " + oldname + " " + newname)
		logo()
		options()
		os.system("cls")
		print("[Failed]Folder not found!")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		renameDir()
	elif not(os.path.exists(os.path.join(os.getcwd(),oldname))):
		os.system("cls")
		print("[Failed]Folder not found!")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		renameDir()
	else:
		os.system("cls")
		print("[Failed]Folder already exists!")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		renameDir()
		
#end of renameDir function
 
#this function is used to delete a folder
def delDir():
	os.system("cls")
	print("================================================")
	print("==================Delete Folder=================")
	print("================================================")
	print("================================================")
	print()
	print("[>]Folder List")
	os.system("dir /ad")
	print()
	name= input ("[?]Folder that you want to delete :")
	if os.path.exists(os.path.join(os.getcwd(),name)):
		os.system("rmdir "+name)
		logo()
		options()
	else:
		os.system("cls")
		print("[Failed]Invalied folder!")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		delDir()
#end of the delDir function

#this function is used to create a file 
def createFile():
	os.system("cls")
	print("================================================")
	print("==================Create File===================")
	print("================================================")
	print("================================================")

	filename = input("[?]Enter file name with extention(ex:myfile.txt) :")
	write =input("[?]If you want to write something write here(if no blank):")
	if os.path.exists(os.path.join(os.getcwd(),filename)):
		os.system("cls")
		print("[Failed]File is already exists!")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		createFile()
	else:
		os.system("echo "+write+" > "+filename)
		logo()
		options()
#end of createFile function

#this function is used to rename a file
def renFile():
	os.system("cls")
	print("================================================")
	print("==================Rename File===================")
	print("================================================")
	print("================================================")
	print()
	print("[>]File List")
	os.system("dir")
	print()
	oldname = input("[?]File name with extention that you want rename :")
	newname = input("[?]New file name with extention :")
	if os.path.exists(os.path.join(os.getcwd(),oldname)) and not(os.path.exists(os.path.join(os.getcwd(),newname))):
			os.system("ren " + oldname + " " + newname)
			logo()
			options()

	elif os.path.exists(os.path.join(os.getcwd(),oldname)) and os.path.exists(os.path.join(os.getcwd(),newname)):
		os.system("cls")
		print("[Failed]File is already exists!")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		renFile()


	elif not(os.path.exists(os.path.join(os.getcwd(),oldname)))and os.path.exists(os.path.join(os.getcwd(),newname)):
		os.system("cls")
		print("[Failed]Invalied file!")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		renFile()

	else:
		os.system("cls")
		print("[Failed]File is already exists!")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		renFile()
#end of renFile function

#this function is used to delete a file
def delFile():
	os.system("cls")
	print("================================================")
	print("==================Delete File===================")
	print("================================================")
	print("================================================")
	print()
	print("[>]File List")
	os.system("dir")
	print()
	name = input("[?]File name with extention :")
	if os.path.exists(os.path.join(os.getcwd(),name)):
		os.system("del " +name)
		logo()
		options()
	else:
		os.system("cls")
		print("[Failed]Invalied file!")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		delFile()
#end of the delFile function

#this funtion is used to write a something on to the file 
def writeFile():
	os.system("cls")
	print("================================================")
	print("==================Write File====================")
	print("================================================")
	print("================================================")
	print()
	print("[>]File List")
	os.system("dir")
	print()
	file_name = input("[?]File name with extention :")
	input_line = input("[?]Write something :")
	if os.path.exists(os.path.join(os.getcwd(),file_name)):
		os.system("echo " +input_line+" > "+file_name)
		logo()
		options()
	else:
		os.system("cls")
		print("[Failed]Invalied file!")
		print("[!]Press any key to go back.")
		os.system("pause>>nul")
		writeFile()
#end of writeFile funtion

#main funtion: it will call logo funtion and options function
def main():
	logo()
	options()
#end of main function

#call the main function
main()