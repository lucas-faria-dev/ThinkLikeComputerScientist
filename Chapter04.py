import turtle
bob = turtle.Turtle()

#bob.fd(100)
#bob.pu()
#bob.lt(45)
#bob.bk(100)
#bob.pd()
#bob.rt(90)
#bob.fd(150)

#bob.fd(100)
#bob.lt(90)
#bob.fd(100)
#bob.lt(135)
#bob.fd(141.4213562373095)

#for i in range(4):
#    bob.fd(100)
#    bob.lt(90)


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()

#square(bob, 10);

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)
    turtle.mainloop()

#polygon(bob, 1, 2)

def circle(t, radius):
    polygon(t, radius, radius * 5)


circle(t=bob, readius=10)