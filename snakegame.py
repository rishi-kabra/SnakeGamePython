import turtle
import time
import random

delay = 0.1

#set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Rishi")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

#Score
score = 0
high_score = 0

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

#funtions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

#main game loop
while True:
    wn.update()

    #checking for border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear the list
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))
         
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #increasing speed
        if delay > 0.02:
            delay -= 0.004

        #Increase the score
        score += 1

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
        


    #Moving segments
    for index in range(len(segments)-1, 0 ,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #adding new segment
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    #Moving 

    move()

    #check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)
            #clear the list
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)





#keeps it in the loop and keeps the screen on
wn.mainloop()