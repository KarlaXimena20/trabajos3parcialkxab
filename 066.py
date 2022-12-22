import turtle
turtle.shape("turtle")

import random
turtle.pensize(3)

for i in range(0,8):
    turtle.color(random.choice(["red","blue","yellow","orange","green","pink"]))
    turtle.forward(50)
    turtle.right(45)

turtle.exitonclick()