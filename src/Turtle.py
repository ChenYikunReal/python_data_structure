from turtle import *


# 递归绘制螺旋线
def drawSpiral(turtle, lineLength):
    if lineLength > 0:
        turtle.forward(lineLength)
        turtle.right(90)
        drawSpiral(turtle, lineLength-5)


# 递归绘制一棵树
def tree(branchLength, turtle):
    if branchLength > 5:
        turtle.forward(branchLength)
        turtle.right(20)
        tree(branchLength-15, turtle)
        turtle.left(40)
        tree(branchLength-10, turtle)
        turtle.right(20)
        turtle.backward(branchLength)


def drawTriangle(points, color, turtle):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(points[1])
    turtle.goto(points[2])
    turtle.goto(points[0])
    turtle.end_fill()


def getMid(p1, p2):
    return ( (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 )


def sierpinski(points, degree, turtle):
    colorMap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colorMap[degree], turtle)
    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree-1, turtle)
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree - 1, turtle)
        sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree - 1, turtle)


myTurtle = Turtle()
myWindow = myTurtle.getscreen()
# drawSpiral(myTurtle, 100)
# myWindow.exitonclick()

# myTurtle.left(90)
# myTurtle.up()
# myTurtle.backward(300)
# myTurtle.down()
# myTurtle.color('green')
# tree(110, myTurtle)
# myWindow.exitonclick()

myPoints = [(-400, -200), (0, 400), (400, -200)]
sierpinski(myPoints, 5, myTurtle)
myWindow.exitonclick()
