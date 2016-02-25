'''
Created on Feb 24, 2016

@author: michael.f.koegel
'''
"""
This is a simple turtle training file. The goal is to make several different shapes.
"""
import turtle #importing the turtle library

def drawSquare(someTurtle): #creating a function for drawing a square
    for i in range(1,5): #a square has 4 sides, so the range starts at 1 and ends at 4
        someTurtle.forward(100) #I want the turtle object to move 100 pixels
        someTurtle.right(90) #I want the turtle to turn in a 90 degree angle

def drawTriangle(someTurtle): #creating a function to draw a tringle
    for i in range(1,4): #a triangle only has 3 sides so the range should only be 3
        someTurtle.forward(100) #I want the turtle to take 100 pixel steps forward
        someTurtle.left(120) #I want the turtle to take 120 dgree turns to make a proper triangle

def drawCircle(someTurtle, size): #defining my circle function
    for i in range(1,2): #only need 1 circle made
        someTurtle.circle(size, None, None) #passing the size value and ignoring the other options for the circle parameters

def drawArt(): #here is where I define the board, turtles, names, etc
    window = turtle.Screen() #creating a screen for the turtle to operate on
    window.bgcolor("red") #defining the background color for our screen
    
    #creating Mike's turtle
    mike = turtle.Turtle() #initializing my turtle
    mike.shape("turtle") #defining the shape of the turtle
    mike.color("green") #defining the color of the turtle
    mike.speed("fastest") #seting the turtle speed
    
    for i in range(1,37): #in order to make a square with a circle in the center, the squares have to go around 36 times
        drawSquare(mike) #passing the turtle mike to the square function
        mike.right(10) #making sure to turn at a 10 degree angle so the circle will appear in the middle of the drawing
    
    #creating Jeannette's turtle
    jeannette = turtle.Turtle() #initializing turtle
    jeannette.shape("arrow") #defining the shape
    jeannette.color("purple") #setting the color
    jeannette.speed("fastest") #setting the speed
    
    for i in range(1,37): #it takes 36 triangles to create a 360 degree circumference
        drawTriangle(jeannette) #passing the turtle Jeannette to the triangle function
        jeannette.right(10) #need to turn at a 10 degree angle to make a 360 degree circle
    
    #creating Annabelle's turtle
    annabelle = turtle.Turtle() #initializing the turtle
    annabelle.shape("turtle") #defining the shape
    annabelle.color("blue") #defining the color
    annabelle.speed("fastest") #defining the speed
    

    for i in range(1,37): #it takes 36 circles to make a 360 degree circle
        drawCircle(annabelle, 100) #passing the turtle name and circle circumference size to the circle function
        annabelle.right(10) #need to turn in a 10 degree angle 36 times
    
    #creating Isabelle's turtle
    isabelle = turtle.Turtle() #initializing the turtle
    isabelle.shape("turtle") #defining the shape
    isabelle.color("black") #defining the color
    isabelle.speed("fastest") #defining the speed
    
    for i in range(1,37): #need this to happen 36 times to make a 360 degree circle
        drawCircle(isabelle, 125) #passing the circle function the turtle name and size of the circle
        isabelle.right(10) #has to make 10 degree turns
    
    window.exitonclick() #only exit the window when the user closes it
    
drawArt() #initializing the program