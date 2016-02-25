'''
Created on Feb 23, 2016

@author: michael.f.koegel
'''
def purify(numbers):
    even = []
    
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    print(even)
    
purify([1,2,3,4,5,6,7,8,9])