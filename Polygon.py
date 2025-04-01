import turtle
turtle.Screen().bgcolor('orange')
turtle.Screen().setup(300,400)
t=turtle.Turtle()

sides=int(input("Enter sides: "))
length=100
angle=360/sides

for i in range(sides):
    t.forward(length)
    t.right(angle)

turtle.mainloop()