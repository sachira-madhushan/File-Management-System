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




logo()
os.system("pause")