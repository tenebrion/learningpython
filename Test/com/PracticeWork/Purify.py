'''
Created on Feb 23, 2016

@author: michael.f.koegel
'''
#the only purpose of this function is to practice removing off numbers while printing out the remaining even numbers
def purify(numbers):
    even = [] #initializing a list
    
    for num in numbers: #iterating through the list of numbers passed to our function
        if num % 2 == 0: #if the number is divisible by 2 without a remainder, it is an even number
            even.append(num) #add it to our list 'even'
    print(even) #print the list
    
purify([1,2,3,4,5,6,7,8,9]) #initializing the function with some numbers to test