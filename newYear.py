import turtle
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
turtle.bgcolor('white')
tr = turtle.Turtle()
tr.speed("fastest")
tr.up()

#left
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(-500,0)
        tr.down()
        tr.color("aqua")
        tr.forward(100)
        tr.circle(5, steps=4)
        tr.right(60)
        tr.color("magenta")
        tr.forward(50)
        tr.right(120)
    tr.right(30)
tr.up()

#right
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(470,0)
        tr.down()
        tr.color("red")
        tr.forward(100)
        tr.circle(5, steps=4)
        tr.right(60)
        tr.color("crimson")
        tr.forward(50)
        tr.right(120)
    tr.right(30)
tr.up()

#top
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(20,265)
        tr.down()
        tr.color("green")
        tr.forward(100)
        tr.circle(5, steps=4)
        tr.right(60)
        tr.color("lime")
        tr.forward(50)
        tr.right(120)
    tr.right(30)
tr.up()

#bottom
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(20,-220)
        tr.down()
        tr.color("dark blue")
        tr.forward(100)
        tr.circle(5, steps=4)
        tr.right(60)
        tr.color("cyan")
        tr.forward(50)
        tr.right(120)
    tr.right(30)

turtle.up()
turtle.color("red")
turtle.goto(-320, 40)
turtle.write("Happy", font=("Cursive", 60))
turtle.goto(-60,40)

turtle.color("deep pink")
turtle.write("New", font=("Aria", 60))
turtle.goto(145,40)

turtle.color("blue")
turtle.write("Year", font=("Aria", 60))
turtle.goto(-74, -60)

turtle.color("green")
turtle.write("2024", font=("Aria", 60))
turtle.done()

# import turtle
# import random

# # Set up screen and turtle
# screen = turtle.Screen()
# screen.setup(width=1.0, height=1.0)
# screen.bgcolor("midnightblue")  # dark background

# tr = turtle.Turtle()
# tr.speed("fastest")

# #  fireworks function
# def create_firework(x, y, color):
#    tr.penup()
#    tr.goto(x, y)
#    tr.pendown()
#    tr.color(color)
#    for i in range(5):
#        tr.forward(50)
#        tr.right(144)

# # colorful spikes around the screen
# for i in range(100):
#    x = random.randint(-500, 500)
#    y = random.randint(-300, 300)
#    color = (random.random(), random.random(), random.random())  # Random colors
#    create_firework(x, y, color)


# tr.penup()
# tr.goto(0, 50)  # Center the text horizontally
# tr.color("gold")
# tr.write("Happy New Year 2024, my dear love", align="center", font=("Monotype Corsiva", 60, "bold"))

# # Hide the turtle
# tr.hideturtle()

# turtle.done()
