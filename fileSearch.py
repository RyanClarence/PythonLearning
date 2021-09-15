###########################################################
#  Author Name : Sboniso Gordon Mziz                      #
###########################################################

import argparse
import os
import re

#create argparse object
argparseObject = argparse.ArgumentParser(description="File and Folder search")
argparseObject.add_argument("-f","--file",help="file name to search",nargs="+",type=str)
argparseObject.add_argument("-d","--dir",help="folder name to search", nargs="+",type=str)
argparseObject.add_argument("-p","--path",help="path to start the search from",default=".",type=str)
groupSelect = argparseObject.add_mutually_exclusive_group()
groupSelect.add_argument("-e","--end",help="Search file that ends with certain characters",action="store_true")
groupSelect.add_argument("-s","--start",help="Search file that start with certain characters",action="store_true")
groupSelect.add_argument("-c","--contain",help="Search file that Contain  certain characters",action="store_true")
value = argparseObject.parse_args()



def fileSearchMatch(pathToSearchFrom,fileToSearchList): 
    for fileToSearch in fileToSearchList:
        walkDataObject = os.walk(pathToSearchFrom)
        for path,_,files in walkDataObject:
            for file in files:
                if file == fileToSearch:
                    print(str(path)+"\\"+str(file))

def fileSearchMatchEnd(pathToSearchFrom,fileToSearchList):
    for fileToSearch in fileToSearchList:
        walkDataObject = os.walk(pathToSearchFrom)
        for path,_,files in walkDataObject:
            for file in files:
                pattern = re.compile(f"{fileToSearch}$")
                if pattern.search(str(file)):
                    print(str(path)+"\\"+str(file))

def fileSearchMatchStart(pathToSearchFrom,fileToSearchList):
     for fileToSearch in fileToSearchList:
        walkDataObject = os.walk(pathToSearchFrom)
        for path,_,files in walkDataObject:
            for file in files:
                pattern = re.compile(f"{fileToSearch}")
                if pattern.search(str(file)):
                    print(str(path)+"\\"+str(file))

def fileSearchMatchContain(pathToSearchFrom,fileToSearchList):
     for fileToSearch in fileToSearchList:
        walkDataObject = os.walk(pathToSearchFrom)
        for path,_,files in walkDataObject:
            for file in files:
                pattern = re.compile(f"{fileToSearch}")
                if pattern.search(str(file)):
                    print(str(path)+"\\"+str(file))

def dirSearchMatch(pathToSearchFrom,dirToSearchList):
    for dirToSearch in dirToSearchList:
        walkDataObject = os.walk(pathToSearchFrom)
        for path,dirs,_ in walkDataObject:
            for dir in dirs:
                if dir == dirToSearch:
                    print(str(path)+"\\"+str(dir))



if __name__ == "__main__":
    print("\n_______________ Files _______________")
    if value.end and value.file != None:
       fileSearchMatchEnd(value.path,value.file)
    if value.start and value.file != None:
        fileSearchMatchStart(value.path,value.file)
    if value.contain and value.file != None:
        fileSearchMatchContain(value.path,value.file)
    elif value.file != None:
       fileSearchMatch(value.path,value.file)
    
    print("\n_______________ Folders ______________")
    if value.dir != None:
        dirSearchMatch(value.path,value.dir)
    