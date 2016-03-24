"""
This is a simple turtle training file. The goal is to make several different shapes.
"""
import turtle


def draw_square(some_turtle):
    """
    Creating a square pattern

    :param some_turtle: str
    """
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_triangle(some_turtle):
    """
    Creating a triangle pattern

    :param some_turtle: str
    """
    for i in range(1,4):
        some_turtle.forward(100)
        some_turtle.left(120)


def draw_circle(some_turtle, size):
    """
    Creating a circle pattern

    :param some_turtle: str
    :param size: num
    """
    for i in range(1,2):
        some_turtle.circle(size, None, None)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    # creating Mike's turtle
    mike = turtle.Turtle()
    mike.shape("turtle")
    mike.color("green")
    mike.speed("fastest")

    # it takes 36 squares to make a complete 360 circle
    for i in range(1,37):
        draw_square(mike)
        mike.right(10)
    
    # creating Jeannette's turtle
    jeannette = turtle.Turtle()
    jeannette.shape("arrow")
    jeannette.color("purple")
    jeannette.speed("fastest")
    
    for i in range(1,37):
        draw_triangle(jeannette)
        jeannette.right(10)
    
    # creating Annabelle's turtle
    annabelle = turtle.Turtle()
    annabelle.shape("turtle")
    annabelle.color("blue")
    annabelle.speed("fastest")

    for i in range(1,37):
        draw_circle(annabelle, 100)
        annabelle.right(10)
    
    # creating Isabelle's turtle
    isabelle = turtle.Turtle()
    isabelle.shape("turtle")
    isabelle.color("black")
    isabelle.speed("fastest")
    
    for i in range(1,37):
        draw_circle(isabelle, 125)
        isabelle.right(10)

    window.exitonclick()

draw_art()  # initializing the program
