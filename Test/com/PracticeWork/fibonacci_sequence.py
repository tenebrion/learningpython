'''
Created on Feb 29, 2016

@author: michael.f.koegel

The entire purpose of this project
is to perform the fibonacci
sequence and practice skills
'''
#n = input("Please enter the sequence 'nth' value: ")

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))