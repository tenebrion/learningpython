'''
Created on Feb 24, 2016

@author: michael.f.koegel
'''
import turtle

def drawSquare(someTurtle):
    for i in range(1,5):
        someTurtle.forward(100)
        someTurtle.right(90)

def drawTriangle(someTurtle):
    for i in range(1,4):
        someTurtle.forward(100)
        someTurtle.left(120)

def drawCircle(someTurtle, size):
    for i in range(1,2):
        someTurtle.circle(size, None, None)

def drawArt():
    window = turtle.Screen()
    window.bgcolor("red")
    
    #creating Mike's turtle
    mike = turtle.Turtle()
    mike.shape("turtle")
    mike.color("green")
    mike.speed("fastest")
    
    for i in range(1,37):
        drawSquare(mike)
        mike.right(10)
    
    #creating Jeannette's turtle
    jeannette = turtle.Turtle()
    jeannette.shape("arrow")
    jeannette.color("purple")
    jeannette.speed("fastest")
    
    for i in range(1,37):
        drawTriangle(jeannette)
        jeannette.right(10)
    
    #creating Annabelle's turtle
    annabelle = turtle.Turtle()
    annabelle.shape("turtle")
    annabelle.color("blue")
    annabelle.speed("fastest")
    

    for i in range(1,37):
        drawCircle(annabelle, 100)
        annabelle.right(10)
    
    #creating Isabelle's turtle
    isabelle = turtle.Turtle()
    isabelle.shape("turtle")
    isabelle.color("black")
    isabelle.speed("fastest")
    
    for i in range(1,37):
        drawCircle(isabelle, 125)
        isabelle.right(10)
    
    window.exitonclick()
    
drawArt()