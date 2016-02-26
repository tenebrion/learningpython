'''
Created on Feb 26, 2016

@author: michael.f.koegel
'''
#codeacademy course to remove duplicate items from a list
def remove_duplicates(value):
    results = [] #creating a blank list
    
    for val in value: #iterating through each item in the value list
        if val not in results: #check to make sure the item isn't already in the results list
            results.append(val) #add the item to the results list if it doesn't exist
    print(results) #printing the results to debug. Otherwise, use return results

remove_duplicates([4,5,4,5])