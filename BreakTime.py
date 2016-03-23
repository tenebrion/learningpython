"""
Created on Mar 7, 2016
@author: Michael Koegel / mkoegel@gmail.com

This is a simple learning program to teach me
how to use the time function and webbrowser function
"""
import webbrowser
import time

count = 0

# printing current time the program started.
print("This program started on: {}".format(time.ctime()))
while count <= 2:
    time.sleep(10)  # this puts the program to sleep based on seconds.
    # opens up a new browser (default system browser) and plays the youtube link
    webbrowser.open_new("https://www.youtube.com/watch?v=SLhZzMgSJJg")
    count += 1