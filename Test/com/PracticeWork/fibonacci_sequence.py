'''
Created on Feb 29, 2016

@author: michael.f.koegel

The entire purpose of this project
is to perform the fibonacci
sequence and practice skills
'''
#n = input("Please enter the sequence 'nth' value: ")

def fibonacci(n):
    """
    Simple and clean method to work on on the
    classic fibonacci sequence
    """
    #assigning x and y at the same time - clean look
    x, y = 0, 1
    values = [] #I wanted to print them in a 'list'
    for i in range(n):
        values.append(x)
        #this eliminates the need for a 'temporary'
        #variable
        x, y = y, x + y
    return values

print(fibonacci(10))