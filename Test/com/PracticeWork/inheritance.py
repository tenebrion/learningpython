'''
Created on Feb 26, 2016

@author: michael.f.koegel

This program is to help me understand inheritance. This was one of the final projects on
Udacity to help understand how they apply to different classes.
'''

#Creating a simple class called parent that contains most of the reusable features
class Parent():
    def __init__(self, last_name, eye_color): #initializing the class with two variables
        print("Parent Constructor Called") #just a debugging feature to see how often the class is called
        self.last_name = last_name #passing variables through
        self.eye_color = eye_color #passing variables through
    
    #print method to show how the child can access the print variable. Note, this will not print the number_of_toys variable for the child
    def show_info(self):
        print("Last Name - " + self.last_name) #simple print message should show Last Name- Cyrus
        print("Eye Color - " + self.eye_color) #print message should show Eye Color - blue

#creating a child class that inherits from the class 'Parent'
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys): #initializing the function and passing variables through it
        print("Child Constructor Called") #print message that will appear every time the child class is called
        Parent.__init__(self, last_name, eye_color) #initializing the Parent class to pass last name and eye color
        self.number_of_toys = number_of_toys #defining number of toys that is seperate from what the parent class contains
    
    #The purpose of this is to show how we can override the show_info in the Parent class and print messages    
    def show_info(self):
        print("Last Name - " + self.last_name) #print message should show Last Name - Cyrus
        print("Eye Color - " + self.eye_color) #print message should show Eye Color - Blue
        print("Number of Toys - " + str(self.number_of_toys)) #print message should show Number Of Toys - 5

#various options getting passed to the two classes.e
billy_cyrus = Parent("Cyrus", "blue")
billy_cyrus.show_info()
miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info()