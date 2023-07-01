import turtle
import time
import random

turtle.title("Snake game")
t=turtle.Turtle()
turtle.bgcolor("black")
t.shape("turtle")
t.color("blue")
t.speed(100)
t.pensize(7)
t.hideturtle()

#drawing border
t.penup()
t.goto(-370,310)
t.pendown()
l=[730,610,730,610]
for i in l:
    t.forward(i)
    t.right(90)

#snake
s=turtle.Turtle()
s.shape("square")
s.shapesize(1,1,5)
s.color("green")
s.speed(10)
s.penup()

#food
f=turtle.Turtle()
f.color("red")
f.shape("square")
f.shapesize(0.8,0.8,5)
f.speed(100)
f.hideturtle()
f.penup()
x=random.randint(-200,200)
y=random.randint(-200,200)
f.goto(x,y)
f.showturtle()

#movement of snake
a=320
b=280
def left():  
    while(True):
        x=s.xcor()
        collision(a,b)
        s.setheading(180)
        s.setx(x-10)
        time.sleep(0.1)
def right():
    while(True):
        x=s.xcor()
        collision(a,b)
        s.setheading(0)
        s.setx(x+10)
        time.sleep(0.1)

def up():
    while(True):
        y=s.ycor()
        collision(a,b)
        s.setheading(90)
        s.sety(y+10)
        time.sleep(0.1)
def down():
    while(True):
        y=s.ycor()
        collision(a,b)
        s.setheading(270)
        s.sety(y-10)
        time.sleep(0.1)

#showing score
turtle.hideturtle()
turtle.penup()
turtle.speed(100)
turtle.color("white")
turtle.setpos(-350,250)

#(global score,Score)
score=0
Score="Score:"+str(score)
turtle.write(Score,move=False,align="left",font=('Courier', 20, 'bold'))

#snake collision
def collision(x,y):    
    if(s.xcor()>a or s.xcor()<-a or s.ycor()>b or s.ycor()<-b):       
        turtle.bye()
        
    if(s.distance(f)<10):
        f.penup()
        x=random.randint(-200,200)
        y=random.randint(-200,200)
        f.goto(x,y)

        #incresing score
        global score
        score+=1      
        s.shapesize(1,score+1,5)
        if(f.pos()==s.pos()):
            f.bye()
            
        Score="Score:"+str(score)
        turtle.clear()
        turtle.write(Score,move=False,align="left",font=('Courier', 20, 'bold'))

#set keys
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.listen()

#turtle.mainloop()
turtle.done()
