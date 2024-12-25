import turtle

def main():
    window = turtle.Screen()
    myTurtle = turtle.Turtle()
    screen = myTurtle.getscreen()
    screen.title("Merry Christmas")
    screen.bgcolor("#120E43")
    
    
    #Draw tree
    myTurtle.color("green")
    myTurtle.pensize(5)
    myTurtle.begin_fill()

    
    #TODO: right half of tree
    myTurtle.forward(100)
    myTurtle.left(150)
    myTurtle.forward(90)
    myTurtle.right(150)
    myTurtle.forward(60)
    myTurtle.left(150)
    myTurtle.forward(60)
    myTurtle.right(150)
    myTurtle.forward(40)
    myTurtle.left(150)
    myTurtle.forward(100)
    
    
    
    #TODO:left half of tree
    myTurtle.left(60)
    myTurtle.forward(100)
    myTurtle.left(150)
    myTurtle.forward(40)
    myTurtle.right(150)
    myTurtle.forward(60)
    myTurtle.left(150)
    myTurtle.forward(60)
    myTurtle.right(150)
    myTurtle.forward(90)
    myTurtle.left(150)
    myTurtle.forward(133)
    myTurtle.end_fill()
    
    
    #TODO: trunk of tree
    myTurtle.color("red")
    myTurtle.pensize(1)
    myTurtle.begin_fill()
    
    myTurtle.right(90)
    myTurtle.forward(70)
    myTurtle.right(90)
    myTurtle.forward(33)
    myTurtle.right(90)
    myTurtle.forward(70)
    myTurtle.end_fill()
    
    def star(trt, x,y,color):
        trt.speed(1)
        trt.penup()
        trt.color(color)
        trt.goto(x,y)
        trt.begin_fill()
        trt.pendown()
    
    
    #create star
    star(myTurtle,-28,110, "yellow")
   
    
    for i in range(5):
        myTurtle.forward(40)
        myTurtle.right(144)

    myTurtle.end_fill()
    
    
    def ball(trt, x, y, size=10, colour="red"):
        trt.penup()
        trt.setpos(x,y)
        trt.color(colour)
        trt.begin_fill()
        trt.pendown()
        trt.circle(size)
        trt.end_fill()
    
    ball(myTurtle, 95,-5)
    ball(myTurtle, -110,-5)
    ball(myTurtle, 80,40, size=7, colour="yellow")
    ball(myTurtle, -98,40, size=7, colour="yellow")
    ball(myTurtle, 70,70, size=5)
    ball(myTurtle, -93, 70, size=5)
    
    
    
    
    
    def createCircle(turtle, x,y, radius, color):
        myTurtle.penup()
        myTurtle.color(color)
        myTurtle.fillcolor(color)
        myTurtle.goto(x,y)
        myTurtle.pendown()
        myTurtle.begin_fill()
        myTurtle.circle(radius)
        myTurtle.end_fill()
        
    createCircle(myTurtle, 230,180,60, "white")
    createCircle(myTurtle, 210, 180, 60, "#120E43")

    
    myTurtle.speed(1)
    myTurtle.penup()
    msg = "Merry Christmas to my wonderful and gorgeous girl!"
    msg2 = "I love u jaan and I will never ever repeat my mistake again..."
    msg3 = "Forgive ME Plz!!!!"
    
    myTurtle.goto(0,-180)
    myTurtle.color("yellow")
    myTurtle.pendown()
    myTurtle.write(msg2, move=False, align="center", font=("Arial", 20, "bold"))
    myTurtle.goto(0,-220)
    myTurtle.color("blue")
    myTurtle.pendown()
    myTurtle.write(msg3, move=False, align="center", font=("Arial", 20, "bold"))
    myTurtle.goto(0,-260)
    myTurtle.color("white")
    myTurtle.pendown()
    myTurtle.write(msg, move=False, align="center", font=("Arial", 25, "bold"))
    
    myTurtle.hideturtle()
    window.mainloop()
        
if __name__ == "__main__":
    main()
    
    
    
        