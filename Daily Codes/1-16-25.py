import turtle
screen = turtle.Screen()
screen.bgcolor("blue") 
donatello = turtle.Turtle() #donatello is mo's favorite TMNT

def square(x, y):
    donatello.pensize(5)
    donatello.pencolor("red")
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    for i in range(4): 
        donatello.forward(50) 
        donatello.right(90)

def triangle(x, y):
    donatello.pensize(10)
    donatello.pencolor("goldenrod")
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    for i in range(3): 
        donatello.forward(70) 
        donatello.right(120)
        
def star(x, y):
    donatello.pensize(10)
    donatello.pencolor("goldenrod")
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    for i in range(5): 
        donatello.forward(75) 
        donatello.right(144)
        
def hexagon(x, y):
    donatello.pensize(10)
    donatello.pencolor("magenta")
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    for i in range(6): 
        donatello.forward(70) 
        donatello.right(60)


def circle(cx, cy, radius):
    donatello.pensize(8)
    donatello.pencolor("turquoise")
    donatello.fillcolor("yellow")
    donatello.penup()
    donatello.goto(cx, cy)
    donatello.pendown()
    donatello.begin_fill()
    donatello.circle(radius)
    donatello.end_fill()
    
#call functions
square(30, 40)
hexagon(100, 200)
square(10, 50)
star(100,87)
triangle (50, 200)
circle(-200, 200, 80)

turtle.done() 
