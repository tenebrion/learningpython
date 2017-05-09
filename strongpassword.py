"""
Just a simple password detection script from Automate the boring stuff

Strong Password Detection
"""
import re


def strong_password(password):
    """
    function that uses regex to make sure the password is strong
    Password must be at least 8 characters long
    Password must have at least 1 digit
    Password must contain one uppercase and one lowercase character
    :param password: 
    :return: True / False
    """
    complex_password_regex = re.compile(r'''(
^(?=.*?[A-Z])           # Checks for uppercase letters
(?=.*?[a-z])            # Checks for lowercase letters
(?=.*?[0-9])            # Checks for a number
(?=.*?[#?!@$%^&*()-_+]) # Checks for special characters
.{8,}$                  # Checks to make sure the password is at least 8 characters long
)''', re.VERBOSE)

    check_password = complex_password_regex.search(password)
    if check_password is None:
        return False
    else:
        return True

print("Please enter a password that is at least 8 characters long:")
user_password = None

while user_password is None:
    new_attempt = input()
    length_requirement = strong_password(new_attempt)
    if length_requirement is False:
        print("Password doesn't meet requirements. Please try again:")
    else:
        user_password = new_attempt
