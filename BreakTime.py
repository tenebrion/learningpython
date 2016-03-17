'''
Created on Feb 24, 2016

@author: michael.f.koegel
'''
"""
This is a simple program to tell me I need a break after a certain period of time.
"""
import webbrowser #needed to work with the webbrowser.open_new function
import time #needed to work with the current time - aka ctime()

count = 0 #counter for the while loop

print("This program started on: " +time.ctime()) #printing current time the program started.
while count <= 2: #as long as the count is less than 2 (technically 3, since code starts at 0)
    time.sleep(3600) #this puts the program to sleep based on seconds.
    webbrowser.open_new("https://www.youtube.com/watch?v=SLhZzMgSJJg") #opens up a new browser (default system browser) and plays the youtube link
    count += 1 #increases the count by 1