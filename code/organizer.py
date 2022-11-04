import os
import winshell
import shutil
import pywintypes
from genericpath import isfile
from importlib.resources import path
import patoolib

imageFormats = ["jpg","png","jpeg","gif","webp","tiff","PNG"]
audioFormats = ["mp3","wav"]
videoFormats = ["mp4","avi","webm","mkv"]
docsFormats = ["txt","epub","pdf","docx","ino","xls","pptx"]
zipFormats = ["rar","zip","7z"]

class cleaner:

    def __init__(self) -> None:
        pass
        
    def cleanBin(self):
        try:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            print("Recycle bin is emptied Now")
        except:
            print("Recycle bin already empty")

        
    def cleanDownloads(self, folder):
        self.folder = folder
        os.chdir(self.folder)
        files = os.listdir("./")

        for file in files:
            if os.path.isfile(file) and file != "cleanStuff.py":
                ext = (file.split(".")[-1]).lower()

                if ext in imageFormats:
                    shutil.move(file, "images/" + file)
                elif ext in audioFormats:
                    shutil.move(file, "audio/" + file)
                elif ext in videoFormats:
                    shutil.move(file, "video/" + file)
                elif ext in docsFormats:
                    shutil.move(file, "docs/" + file)
                elif ext in zipFormats:
                    shutil.move(file, "zip/" + file)
                else:
                    shutil.move(file, "others/" + file)


    def move_stuff(self, origin, destiny, Anyformat):
        self.origin = origin
        self.destiny = destiny
        self.Anyformat = Anyformat

        os.chdir(self.origin)
        files = os.listdir("./")

        for file in files:
            if os.path.isfile(file) and file != "cleanStuff.py":
                ext = (file.split(".")[-1]).lower()
                if ext in self.Anyformat:
                    shutil.move(self.file, self.destiny + file)
                else:
                    return

    def extract_zip(self, folder, destiny):
        self.folder = folder
        self.destiny = destiny

        os.chdir(self.folder)
        files = os.listdir("./")

        for file in files:
            if os.path.isfile(file) and file != "cleanStuff.py":
                ext = (file.split(".")[-1]).lower()
                if ext in zipFormats:
                    patoolib.extract_archive(file, outdir = self.destiny)
                else:
                    return

    def remove_files(self, origin, Anyformat):
        self.origin = origin
        self.Anyformat = Anyformat

        os.chdir(self.origin)
        files = os.listdir("./")

        for file in files:
            if os.path.isfile(file) and file != "cleanStuff.py":
                ext = (file.split(".")[-1]).lower()

                if ext in self.Anyformat:
                    os.remove(file)
                else:
                    return
