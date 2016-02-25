'''
Created on Feb 25, 2016

@author: michael.f.koegel
'''
import urllib.request

def readText():
    quotes = open(r"C:\Users\michael.f.koegel\Documents\Python\MovieQuotes.txt")
    contentsOfFile = quotes.read()
    #print(contentsOfFile)
    quotes.close()
    checkProfanity(contentsOfFile)
    
def checkProfanity(textToCheck):
    connection = urllib.request.urlopen("http://www.wdyl.com/profanity?q="+textToCheck)
    output = connection.read()
    #print(output)
    connection.close()
    
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly!")
    
readText()