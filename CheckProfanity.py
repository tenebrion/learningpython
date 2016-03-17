'''
Created on Feb 25, 2016

@author: michael.f.koegel
'''
#need to import the urllib file to open URLs
import urllib.request

#defining my function that will read text from a .txt file
def readText():
    quotes = open(r"C:\Users\michael.f.koegel\Documents\Python\MovieQuotes.txt") #actually opening the file
    contentsOfFile = quotes.read() #this will read the file
    #print(contentsOfFile) #debugging via print method
    quotes.close() #closing the file so it doesn't remain open in memory
    checkProfanity(contentsOfFile) #passing the file to the checkProfanity function

#this function actually connect to the web site to check for profanity in our text document
def checkProfanity(textToCheck):
    connection = urllib.request.urlopen("http://www.wdyl.com/profanity?q="+textToCheck) #opening the url
    output = connection.read() #reading the site
    #print(output) #debugging mode via print
    connection.close() #closing the connection
    
    if "true" in output: #if the site says there is profanity, it will print a message
        print("Profanity Alert!!")
    elif "false" in output: #if the site says there is no profanity, prints a message
        print("This document has no curse words!")
    else: #otherwise the file cannot be read
        print("Could not scan the document properly!")
    
readText() #initializing the method