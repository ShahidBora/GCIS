import turtle
def circle(x,y,radius,color):
    turtle.penup()
    turtle.goto(x,y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
def main():
    circle(0,0,100,"blue")
    circle(0,-20,20,"red")
    #draw_nose
    #draw_eye(1)
    #draw_eye(2)
    pass
main()