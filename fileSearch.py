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
    for path,_,files in walkDataObject:
        for file in files:
            if file == fileToSearch:
                print(str(path)+"\\"+str(file))

def dirSearch(pathToSearchFrom,dirToSearch):
    walkDataObject = os.walk(pathToSearchFrom)
    for path,dirs,_ in walkDataObject:
        for dir in dirs:
            if dir == dirToSearch:
                 print(str(path)+"\\"+str(dir))

if __name__ == "__main__":
    print("\n_______________ Files _______________")
    if value.file != None:
        fileSearch(value.path,value.file)
    
    print("\n_______________ Folders ______________")
    if value.dir != None:
        dirSearch(value.path,value.dir)
