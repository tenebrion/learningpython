"""
Created on Feb 26, 2016

@author: michael.f.koegel

This program is to help me understand inheritance. This was one of the final projects on
Udacity to help understand how they apply to different classes.
"""


class Parent():
    """
    Creating a simple class called parent that contains most of the reusable features
    """
    def __init__(self, last_name, eye_color):
        """
        setting up variables for our Parent class

        :param last_name: str
        :param eye_color: str
        """
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        """
        print method to show how the child can access the print variable.
        Note, this will not print the number_of_toys variable for the child
        """
        print("Last Name - " + self.last_name)  # Last Name- Cyrus
        print("Eye Color - " + self.eye_color)  # Eye Color - blue


class Child(Parent):
    """
    creating a child class that inherits from the class 'Parent'
    """
    def __init__(self, last_name, eye_color, number_of_toys):
        """
        defining variables to demonstrate inheritance

        :param last_name: str
        :param eye_color: str
        :param number_of_toys: num
        """
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        """
        The purpose of this is to show how we can override the show_info in the
        Parent class and print messages

        :param self:
        """
        print("Last Name - " + self.last_name)  # Last Name - Cyrus
        print("Eye Color - " + self.eye_color)  # Eye Color - Blue
        print("Number of Toys - " + str(self.number_of_toys))  # Number Of Toys - 5

# various options getting passed to the two classes.e
billy_cyrus = Parent("Cyrus", "blue")
billy_cyrus.show_info()
miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info()