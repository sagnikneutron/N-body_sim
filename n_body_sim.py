import turtle 
import math 
import random 
import numpy
sc = turtle.Screen()
sc.bgcolor('black')
sc.tracer(0)
global BODIES, G 
BODIES = []
G =float(6.67*pow(10,-11))
class body():
    global turtlee
    def __init__(self,mass,bodyn,xvel,yvel,xcor,ycor,diameter):
        self.mass = mass 
        self.bodyn=bodyn
        self.xvel = xvel 
        self.diameter=diameter
        self.yvel = yvel
        self.xcor = xcor
        self.ycor = ycor
        global turtlee 
        turtlee = turtle.Turtle()
        turtlee.shape('circle')
        turtlee.setpos(self.xcor,self.ycor)
        turtlee.shapesize(self.diameter)
        turtlee.color(random.choice(['red','green','blue','purple','yellow']))
        turtlee.penup()
    def pendown():
        global turtlee 
        turtlee.pendown()
    def penup():
        global turtlee
        turtlee.penup()
def determinevector(body):
    global G 
    listx = []
    listy=[]
    for bodyn in BODIES:
        x1,y1,m1 = bodyn.xcor,bodyn.ycor,bodyn.mass
        x2,y2,m2 = body.xcor,body.ycor, body.mass
        fg=z2
        z2 = float(G*m1*m2)/float(abs(x2-x1))^2+float(abs(y2-y1)^2)
        z1 = float(abs(x2-x1))^2+float(abs(y2-y1)^2)
        x = float(z2/z1)*abs(x2-x1)
        y = float(z2/z1)*abs(y2-y1)
        listx.append(x)
        listy.append(y)
    body.xvel = sum(listx)
    body.yvel = sum(listy)
print('mass,xvel,yvel,xcor,ycor,diameter')
n = input('number of bodies : ')
for i in range(0,int(n)):
    mass,xvel,yvel,xcor,ycor,diameter=input().split('')
    BODIES.append(body(mass,len(BODIES),xvel,yvel,xcor,ycor,diameter))
while True:
    sc.update()
    for body in BODIES:
        determinevector(body)
