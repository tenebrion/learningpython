'''
Created on Feb 24, 2016

@author: michael.f.koegel
'''
#need to import the os functions to gain access to chdir, getcwd, listdir, rename, etc.
import os

def rename_files(): #the function will work with all files located in a specific path and strip out numbers from the file name
    fileList = os.listdir(r"C:\Users\michael.f.koegel\Downloads\prank") #defining path to files
        
    oldDir = os.getcwd() #grabbing the current working directory
    os.chdir(r"C:\Users\michael.f.koegel\Downloads\prank") #changing directory to the location of the files
    
    for fileName in fileList: #iterating through each file
        print("Renaming file " + fileName) #printing existing file names
        print("New Name - " + fileName.translate("0123456789")) #printing new file names
        os.rename(fileName, fileName.translate(None,"0123456789")) #stripping out all numbers from the file names
    os.chdir(oldDir) #setting the working directory back to the original path 'oldDir'

rename_files() #initializing the program