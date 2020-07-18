import turtle
import time
import random

delay = 0.1

#set up the screen
wn = turtle.Screen()
wn.title("Snake Game - Multi Player by Rishi")
wn.bgcolor("green")
wn.setup(width=900, height=900)
wn.tracer(0)

#snake head1
a = turtle.Turtle()
a.speed(0)
a.shape("square")
a.color("black")
a.penup()
a.goto(100,0)
a.direction = "stop"

#snake head2
b = turtle.Turtle()
b.speed(0)
b.shape("square")
b.color("blue")
b.penup()
b.goto(-100,0)
b.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
x = random.randint(-430,430)
y = random.randint(-430,430)        
food.goto(x,y)

#bodies of A and B
segments_a = []
segments_b = []

#Score/Info Writing
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Welcome - Use WASD and ARROWS", align="center", font=("Courier", 24, "normal"))

#funtions

def go_up():
    if a.direction != "down":
        a.direction = "up"

def go_down():
    if a.direction != "up":
        a.direction = "down"

def go_right():
    if a.direction != "left":
        a.direction = "right"

def go_left():
    if a.direction != "right":
        a.direction = "left"

def go_up_b():
    if b.direction != "down":
        b.direction = "up"

def go_down_b():
    if b.direction != "up":
        b.direction = "down"

def go_right_b():
    if b.direction != "left":
        b.direction = "right"

def go_left_b():
    if b.direction != "right":
        b.direction = "left"


def move_a():
    if a.direction == "up":
        y = a.ycor()
        a.sety(y+20)

    if a.direction == "down":
        y = a.ycor()
        a.sety(y-20)

    if a.direction == "left":
        x = a.xcor()
        a.setx(x-20)

    if a.direction == "right":
        x = a.xcor()
        a.setx(x+20)


def move_b():
    if b.direction == "up":
        y = b.ycor()
        b.sety(y+20)

    if b.direction == "down":
        y = b.ycor()
        b.sety(y-20)

    if b.direction == "left":
        x = b.xcor()
        b.setx(x-20)

    if b.direction == "right":
        x = b.xcor()
        b.setx(x+20)


#keyboard bindings/inputs
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_up_b, "w")
wn.onkeypress(go_down_b, "s")
wn.onkeypress(go_right_b, "d")
wn.onkeypress(go_left_b, "a")

#main game loop
while True:
    wn.update()

    #checking for borderA
    if a.xcor()>440 or a.xcor()<-440 or a.ycor()>440 or a.ycor()<-440:
        time.sleep(1)
        a.goto(100,0)
        a.direction = "stop"
        b.goto(-100,0)
        b.direction = "stop"
        #hide the segments
        for segment in segments_a:
            segment.goto(1000,1000)
        for segment in segments_b:
            segment.goto(1000,1000)
        #clear the list
        segments_a.clear()
        segments_b.clear()
        pen.clear()
        pen.write("B won - Use WASD and ARROWS", align="center", font=("Courier", 24, "normal"))

    #checking for borderB
    if b.xcor()>440 or b.xcor()<-440 or b.ycor()>440 or b.ycor()<-440:
        time.sleep(1)
        a.goto(100,0)
        a.direction = "stop"
        b.goto(-100,0)
        b.direction = "stop"
        #hide the segments
        for segment in segments_a:
            segment.goto(1000,1000)
        for segment in segments_b:
            segment.goto(1000,1000)
        #clear the list
        segments_a.clear()
        segments_b.clear()
        pen.clear()
        pen.write("A won - Use WASD and ARROWS", align="center", font=("Courier", 24, "normal"))
         
    
    #eating foodA
    if a.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-430,430)
        y = random.randint(-430,430)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments_a.append(new_segment)

        #increasing speed
        if delay > 0.02:
            delay -= 0.001
        
        pen.clear()
        pen.write("A became bigger", align="center", font=("Courier", 24, "normal")) 

    if b.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-430,430)
        y = random.randint(-430,430)        
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments_b.append(new_segment)

        #increasing speed
        if delay > 0.02:
            delay -= 0.001
      
        pen.clear()
        pen.write("B became bigger", align="center", font=("Courier", 24, "normal")) 
        


    #Moving segmentsA
    for index in range(len(segments_a)-1, 0 ,-1):
        x = segments_a[index-1].xcor()
        y = segments_a[index-1].ycor()
        segments_a[index].goto(x,y)

    #adding new segmentA
    if len(segments_a) > 0:
        x = a.xcor()
        y = a.ycor()
        segments_a[0].goto(x,y)

    #Moving segmentsB
    for index in range(len(segments_b)-1, 0 ,-1):
        x = segments_b[index-1].xcor()
        y = segments_b[index-1].ycor()
        segments_b[index].goto(x,y)

    #adding new segmentA
    if len(segments_b) > 0:
        x = b.xcor()
        y = b.ycor()
        segments_b[0].goto(x,y)


    #Moving 
    move_a()
    move_b()

    #check for head collision with the body segments
    for segment in segments_a:
        if segment.distance(a) <20:
            time.sleep(1)
            a.goto(100,0)
            a.direction = "stop"
            b.goto(-100,0)
            b.direction = "stop"
            #hide the segments
            for segment in segments_a:
                segment.goto(1000,1000)
            #clear the list
            segments_a.clear()
            segments_b.clear()
            delay = 0.1
            pen.clear()
            pen.write("B won", align="center", font=("Courier", 24, "normal"))

    for segment in segments_b:
        if segment.distance(a) <20:
            time.sleep(1)
            a.goto(100,0)
            a.direction = "stop"
            b.goto(-100,0)
            b.direction = "stop"
            #hide the segments
            for segment in segments_a:
                segment.goto(1000,1000)
            #clear the list
            segments_a.clear()
            segments_b.clear()
            delay = 0.1
            pen.clear()
            pen.write("B won", align="center", font=("Courier", 24, "normal"))

    for segment in segments_a:
        if segment.distance(b) <20:
            time.sleep(1)
            a.goto(100,0)
            a.direction = "stop"
            b.goto(-100,0)
            b.direction = "stop"
            #hide the segments
            for segment in segments_a:
                segment.goto(1000,1000)
            #clear the list
            segments_a.clear()
            segments_b.clear()
            delay = 0.1
            pen.clear()
            pen.write("A won", align="center", font=("Courier", 24, "normal"))

    for segment in segments_b:
        if segment.distance(b) <20:
            time.sleep(1)
            a.goto(100,0)
            a.direction = "stop"
            b.goto(-100,0)
            b.direction = "stop"
            #hide the segments
            for segment in segments_a:
                segment.goto(1000,1000)
            #clear the list
            segments_a.clear()
            segments_b.clear()
            delay = 0.1
            pen.clear()
            pen.write("A won", align="center", font=("Courier", 24, "normal"))

    if a.distance(b) == 0:
            time.sleep(1)
            a.goto(100,0)
            a.direction = "stop"
            b.goto(-100,0)
            b.direction = "stop"
            #hide the segments
            for segment in segments_a:
                segment.goto(1000,1000)

            #clear the list
            segments_a.clear()
            segments_b.clear()
            delay = 0.1
            pen.clear()
            pen.write("Its a Draw", align="center", font=("Courier", 24, "normal"))


    
            
            
            
            
    time.sleep(delay)





#keeps it in the loop and keeps the screen on
wn.mainloop()

