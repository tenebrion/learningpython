'''
Created on Feb 26, 2016

@author: michael.f.koegel
'''
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    
    for score in scores:
        total += score
    print(total)

grades_sum(grades)