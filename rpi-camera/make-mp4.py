import os
import datetime
dt = datetime.datetime.now()

def getDateString():
	dt = datetime.datetime.now()
	yr = dt.year
	hr = dt.hour
	minute = dt.minute
	sec = dt.second
	timestring = str(dt.month) + "-" + str(dt.day) + "-" + str(yr)+ "-" +str(hr)+ "-" +str(minute)+ "-" +str(sec)
	return timestring






def ffmpeg1():
	filename = getDateString()
	filename = "../videos/" + filename + ".mp4"	
	#os.system(date)
	os.system("cd pics/;ffmpeg -framerate 10 -i image-%05d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p "+filename)
	os.system("date")




ffmpeg1()


'''

ffmpeg -framerate 10 -i image-%05d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4

a=1
for i in *.jpg; do
  new=$(printf "image-%05d.jpg" "$a") #04 pad to length of 4
  mv -i -- "$i" "$new"
  let a=a+1
done
'''
