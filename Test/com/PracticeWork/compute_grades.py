'''
Created on Feb 26, 2016

@author: michael.f.koegel

This is going to turn into a simple grade book that performs
certain calculations based on a set list (or a list that gets
passed to the  grades_sum function).
'''
#defining the hard coded list
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print(grade)

def grades_sum(grades):
    total = 0
    
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    
    for score in scores:
        variance += ((average - score) ** 2)
    
    return average / len(scores)

def grades_std_deviation(variance):
    return (variance ** 0.5)
    
variance = grades_variance(grades)
#print("The list of grades: " + str(print_grades(grades)))
print("The sum of the grades is " + str(grades_sum(grades)))
print("The average of the grades is " + str(grades_average(grades)))
print("The grade variance is " + str(grades_variance(grades)))
print("The grade standard deviation is " + str(grades_std_deviation(variance)))