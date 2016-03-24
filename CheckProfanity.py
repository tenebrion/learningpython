"""
Created on Feb 25, 2016

@author: michael.f.koegel
"""
import urllib.request


def read_text():
    """
    This method simple opens the file and reads it, then passes the info
    off to check for profanity.
    """
    quotes = open(r"C:\Users\michael.f.koegel\Documents\Python\MovieQuotes.txt")
    contentsOfFile = quotes.read()
    quotes.close()
    check_profanity(contentsOfFile)


def check_profanity(text_check):
    """
    This method opens a connection to a site and checks to see if our
    content has profanity. If it does, a message stating so is produced.

    :param text_check: str
    """
    connection = urllib.request.urlopen("http://www.wdyl.com/profanity?q=" + text_check)
    output = connection.read()
    connection.close()
    
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly!")
    
read_text()
