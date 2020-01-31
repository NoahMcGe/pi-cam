import os
os.system("date")


def run():
	print("All files will download where is the install file is located so please put it into a separate directory with no other files. ^-^")
	a = input ("Would you like to download the the pi-cam files? (Y/N): ")
	if (a == "Y" or a == "y"):
		os.system("mkdir pics")
		os.system("cd img/;wget https://raw.githubusercontent.com/NoahMcGe/python/master/2019-2020/turtle/Plot-Line-Circle/img/42.png")
		os.system("wget https://raw.githubusercontent.com/NoahMcGe/python/master/2019-2020/turtle/Plot-Line-Circle/run.py")
		os.system("date")
	elif (a == "N" or a == "n"):
		run3()
		exit()
	else:
		run()
	
def run3():
	a = input ("Would you like to display the credits? (Y/N): ")
	if (a == "Y" or a == "y"):
		print("Noah McGehee")
		print("Mr. Coleman")
	elif (a == "N" or a == "n"):
		print("did not display credits.")
	else:
		run3()

def run4():
	a = input ("Would you like to download instructions? (Y/N): ")
	if (a == "Y" or a == "y"):
		os.system("wget https://raw.githubusercontent.com/NoahMcGe/python/master/2019-2020/turtle/Plot-Line-Circle/instructions.txt")
		
	elif (a == "N" or a == "n"):
		print("did not download instructions.")
	else:
		run4()
		



run()
run4()
run3()

os.system("rm install.py")
