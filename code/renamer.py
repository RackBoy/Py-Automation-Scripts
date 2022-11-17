from pathlib2 import Path
import os

'''
before use. pip install pathlib2
d main pourpose of this class is rename random stuff, such as images, files and so on.
keep in mind this is a previous version, so it might contains bugs
plis, report to d creator
'''


class namer:
    def __init__(self, path):
        self.path = path
        self.p = Path(self.path)

    def done(func):
        def wrapper(*args):
            func(*args)
            print("Files renamed")
        return wrapper


#it receives either a folder or a single file. 
# use same path as constructor to keep files there or another to move'em
    @done
    def renameFiles(self, pathh): 
        self.pathh = pathh
        size = 0    
        if os.path.isdir(self.pathh): #4 a whole directory
            for x in self.p.iterdir():
                new_name = self.pathh + str(size) + "_" + x.name
                os.rename(x,new_name)
                size +=1
        else:
            try:
                new_name = self.pathh + str(size) + "_" + x.name #4 a single file
                os.rename(pathh,new_name)
            except FileExistsError:
                print("File already exists")
                os.remove(new_name)
                os.rename(pathh, new_name)

#it renames files with an specific keyword
    @done
    def renameFilesPattern(self, pathh, pattern):
        self.pathh = pathh
        self.pattern = pattern
        size = 0    
        if os.path.isdir(self.pathh): #4 a whole directory
            for x in self.p.iterdir():
                new_name = self.pathh + self.pattern + "_" + str(size) + x.suffix
                os.rename(x,new_name)
                size +=1
                
        else:
            try:
                new_name = self.pathh + self.pattern + "_" + x.suffix #4 a single file
                os.rename(pathh,new_name)
            except FileExistsError:
                print("File already exists")
                os.remove(new_name)
                os.rename(pathh, new_name)


    #it cleans up current name of file and replaces it with a number
    @done
    def renameFilesSimple(self, pathh):
        self.pathh = pathh
        size = 0    
        if os.path.isdir(self.pathh): #4 a whole directory
            for x in self.p.iterdir():
                new_name = self.pathh + str(size) + x.suffix
                os.rename(x,new_name)
                size +=1
                
        else:
            try:
                new_name = self.pathh +str(size) + x.suffix #4 a single file
                os.rename(pathh,new_name)
            except FileExistsError:
                print("File already exists")
                os.remove(new_name)
                os.rename(pathh, new_name)

    #this method changes d extension of a file. note: not tested completely
    def changeExtension(self, pathh, ext):
        self.pathh = pathh
        self.ext = ext
        if os.path.isdir(self.pathh): #4 a whole directory
            for x in self.p.iterdir():
                new_name = self.pathh.replace(x.suffix, self.ext)
                #new_name = self.pathh + str(size) + x.suffix
                os.rename(x,new_name)
        else:
            try:
                new_name = self.pathh.replace(x.suffix, self.ext) #4 a single file
                os.rename(pathh,new_name)
            except FileExistsError:
                print("File already exists")
                os.remove(new_name)
                os.rename(pathh, new_name)
