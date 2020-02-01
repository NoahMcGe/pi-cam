import os
os.system("date")


def f1open():
	print(" All files will download where is the install file is located so please put it into a separate directory. ^-^")
	a = input ("Would you like to download the the pi-cam files? (Y/N): ")
	if (a == "Y" or a == "y"):
		os.system("mkdir rpi-camera")
		os.system("cd rpi-camera/;mkdir pics/")
		os.system("cd rpi-camera/;mkdir videos/")
		os.system("cd rpi-camera/;wget install.py")
		os.system("cd rpi-camera/;wget rpi-camera/make-mp4.py")
		os.system("date")
	elif (a == "N" or a == "n"):
		exit()
	else:
		f1open()
		
def f4dependencies():
	a = input ("would you like to install dependencies? (Y/N): ")
	if (a == "Y" or a == "y"):
		f5ffmpeg()
	elif (a == "N" or a == "n"):
		f2credits()
	else:
		f4install()		
		

def f5ffmpeg():
	a = input ("would you like to install ffmpeg? (Y/N): ")
	if (a == "Y" or a == "y"):
		os.system("date")
		os.system("sudo apt install ffmpeg -y")
		os.system("date")
	elif (a == "N" or a == "n"):
		print("did not install ffmpeg.")
	else:
		f4install()	




	
def f2credits():
	a = input ("Would you like to display the credits? (Y/N): ")
	if (a == "Y" or a == "y"):
		print("Noah McGehee")
	elif (a == "N" or a == "n"):
		print("did not display credits.")
	else:
		f2credits()

def f3instructions():
	a = input ("Would you like to download instructions? (Y/N): ")
	if (a == "Y" or a == "y"):
		os.system("cd rpi-camera/;wget instructions")
		
	elif (a == "N" or a == "n"):
		print("did not download instructions.")
		
	else:
		f3instructions()
		
def f6end():
	os.system("date")


def main():
	f1open()
	f3instructions()
	f4dependencies()
	f2credits()
	f6end()


main()

