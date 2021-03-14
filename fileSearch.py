import argparse
import os

#create argparse object
argparseObject = argparse.ArgumentParser(description="File and Folder search")
argparseObject.add_argument("-f","--file",help="file name to search",nargs="?",type=str)
argparseObject.add_argument("-d","--dir",help="folder name to search", nargs="?",type=str)
argparseObject.add_argument("-p","--path",help="path to start the search from",default=".",type=str)
value = argparseObject.parse_args()


def fileSearch(pathToSearchFrom,fileToSearch): 
    walkDataObject = os.walk(pathToSearchFrom)
    for _,_,files in walkDataObject:
        for file in files:
            if file == fileToSearch:
                print(file)

def dirSearch(pathToSearchFrom,dirToSearch):
    walkDataObject = os.walk(pathToSearchFrom)
    for _,dirs,_ in walkDataObject:
        for dir in dirs:
            if dir == dirToSearch:
                print(dir)

if __name__ == "__main__":
    if value.file != None:
        fileSearch(value.path,value.file)
    if value.dir != None:
        dirSearch(value.path,value.dir)
