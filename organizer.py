import os
import shutil
import pywintypes
from win10toast import ToastNotifier

imageFormats = ["jpg","png","jpeg","gif","webp","tiff"]
audioFormats = ["mp3","wav"]
videoFormats = ["mp4","avi","webm","mkv"]
docsFormats = ["txt","epub","pdf","doc","ino","xls"]

#toast = ToastNotifier()
#toast.show_toast("File organizer running",duration=20) #show notification on win

#line to create a folder or directory
# os.makedirs("music")

os.chdir("C:\\Users\\brahi\\Downloads")

while True:
	files = os.listdir("./")

	for file in files:
		if os.path.isfile(file) and file != "organizer.py" : #when is runin with win startup put this: and file != organizer.bat and file != organizer.vbs
			ext = (file.split(".")[-1]).lower()

			if ext in imageFormats:
				shutil.move(file,"images/"+file)
			elif ext in audioFormats:
				shutil.move(file,"audio/"+file)
			elif ext in videoFormats:
				shutil.move(file,"video/"+file)
			elif ext in docsFormats:
				shutil.move(file,"docs/"+file)
			else:
				shutil.move(file,"others/"+file)
