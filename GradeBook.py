'''
Created on Feb 24, 2016

@author: michael.f.koegel
'''
"""
The purpose of this is to practice working with lists.
"""
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Function to get the average of the scores
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)

# function to get the student's average score and return the results
def get_average(student):
    homework = average(student["homework"]) # getting averages of the homework
    quizzes = average(student["quizzes"]) # getting averages of the quizzes
    tests = average(student["tests"]) # getting averages of the tests
    
    # homework is only worth 10% of the overall grade
    # quizzes are worth 30% of the overall grade
    # tests are worth 60% of the overall grade
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests # adding each weighted score

# converting the scores to a letter grade
def get_letter_grade(score): # a future version could limit this to an int only
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# getting the average of the entire class scores
def get_class_average(students):
    results = []
    
    for member in students: # looping over all the students passed through
        results.append(get_average(member)) # adding the results to the 'results' table
    
    return average(results)

# this section is printing out results
print(get_letter_grade(get_average(lloyd))) # should return a B
#print(get_class_average(lloyd)) # should return ~89.
#print(get_letter_grade(score)) # should return B