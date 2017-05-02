"""
The purpose of this is to practice working with lists and dictionaries.
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


def average(numbers):
    """
    Function to get the average of the scores

    :param numbers: num
    """
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)


def get_average(student):
    """
    function to get the student's average score and return the results

    :param student: str
    """
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])

    # homework is only worth 10% of the overall grade
    # quizzes are worth 30% of the overall grade
    # tests are worth 60% of the overall grade
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests


def get_letter_grade(score):
    """
    converting the scores to a letter grade

    :param score: num
    """
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


def get_class_average(students):
    """
    getting the average of the entire class scores

    :param students: str
    """
    results = []

    for member in students:
        results.append(get_average(member))

    return average(results)

# this section is printing out results
student_letter_grade = get_letter_grade(get_average(lloyd))
class_average = get_class_average(lloyd)
grade = get_letter_grade(student_letter_grade)
print(student_letter_grade)  # should return a B
print(class_average)  # should return ~89.
print(grade)  # should return B
