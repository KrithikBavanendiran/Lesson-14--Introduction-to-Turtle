import turtle
turtle.Screen().bgcolor('orange')
turtle.Screen().setup(300,400)
t=turtle.Turtle()

for i in range(3):
    t.fd(100)
    t.lt(120)
t.lt(90)
t.penup()
t.fd(50)
t.right(90)
t.pendown()
for i in range(3):
    t.fd(100)
    t.rt(120)

t.ht()
turtle.mainloop()