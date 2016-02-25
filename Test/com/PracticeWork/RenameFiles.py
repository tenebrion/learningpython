'''
Created on Feb 24, 2016

@author: michael.f.koegel
'''
import os

def rename_files():
    fileList = os.listdir(r"C:\Users\michael.f.koegel\Downloads\prank")
        
    oldDir = os.getcwd()
    os.chdir(r"C:\Users\michael.f.koegel\Downloads\prank")
    
    for fileName in fileList:
        print("Renaming file " + fileName)
        print("New Name - " + fileName.translate("0123456789"))
        os.rename(fileName, fileName.translate(None,"0123456789"))
    os.chdir(oldDir)

rename_files()