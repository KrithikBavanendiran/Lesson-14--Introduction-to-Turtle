import turtle
turtle.Screen().bgcolor('orange')
turtle.Screen().setup(300,400)
t=turtle.Turtle()

sides=4
length=100
angle=90

for i in range(sides):
    t.forward(length)
    t.right(angle)

turtle.mainloop()