import turtle
from turtle import Turtle,Screen
import os

screen = Screen()
screen.setup(800,600)
screen.bgpic(os.path.join('../styles/draw_game_style', 'screentry2.gif'))
# screen.register_shape(os.path.join('draw_game_style', 'xx (1).gif'))
t = Turtle("arrow")
t.speed(0)
black = "black"
red = "red"
green = "green"
pink = "pink"
blue = "blue"
start_list  = []
start = True

def up():
    t.setheading(90)
    start_list.append("up")

def down():
    t.setheading(270)
    start_list.append("down")

def right():
    t.setheading(0)
    start_list.append("right")

def left():
    t.setheading(180)
    start_list.append("left")

def control_z():
    t.undo()
    start_list.append("z")

def hide():
    if t.isvisible() == True:
        t.hideturtle()
    else:
        t.showturtle()

def make_circle():
    t.setheading(t.heading() - 90)
    t.circle(40)

def make_dot():
    t.setheading(t.heading() - 90)
    t.dot(40)

def make_square():
    t.begin_fill()
    for i in range(4):
        t.forward(40)
        t.right(90)
    t.end_fill()

def heart():
    t.right(90)
    t.width(3)
    t.color("black","red")
    t.begin_fill()
    t.left(50)
    t.forward(60)
    t.circle(22.5,200)
    t.left(220)
    t.circle(22.5,200)
    t.forward(60)
    t.end_fill()
    start_list.append("heart")

def add_to_file(color_or_pos):
    start_list.append(color_or_pos)

def draw_Square(color):
    t.color("black",str(color))
    t.begin_fill()
    for i in range(4):
        t.forward(45)
        t.right(90)
    t.end_fill()

def draw_rectangle(widt,x):
    t.color("black")
    t.width(3)
    for i in range(1,5):
        if i % 2 == 0:
            t.forward(widt)
            t.right(90)
        else:
            t.forward(40)
            t.right(90)
    t.width(1)
    t.penup()
    if x == 1:
        t.forward(10)
    t.right(90)
    t.forward(10)
    t.pendown()

def dragging(x,y):
    if True:
        if 129 < x < 174 and -274 < y < -229:
            t.color(red)
            add_to_file(red)
        elif 173 < x < 218 and -274 < y < -229:
            t.color(green)
            add_to_file(green)
        elif 219 < x < 263 and -274 < y < -229:
            t.color(blue)
            add_to_file(blue)
        elif 263 < x < 308 and -274 < y < -229:
            t.color(pink)
            add_to_file(pink)
        elif 309 < x < 353 and -274 < y < -229:
            t.color(black)
            add_to_file(black)
        elif 140 < x < 241 and -225 < y < -185:
            w = t.width()
            t.width(w + 2)
            add_to_file(str(w + 2))
        elif 240 < x < 330 and -230 < y < -189:
            w = t.width()
            if w >= 3:
                t.width(w - 2)
                add_to_file(str(w - 2))
        elif -100 < x < 20 and -270 < y < -228:
            t.penup()
            add_to_file("penup")
        elif -100 < x < 20 and -230 < y < -187:
            t.pendown()
            add_to_file("pendown")
        elif -350 < x < -195 and -273 < y < -230:
            screen.reset()
            t.left(90)
            start_list.clear()
        elif 159 < x < 361 and 228 < y < 271:
            download()
        elif -351 < x < -174 and 228 < y < 271:
            upload()
        else:
            dirc = t.heading()
            try:
                t.setheading(t.towards(x, y))
                dirc = t.heading()
            except:
                pass
            t.goto(x, y)
            xx = t.xcor()
            yy = t.ycor()
            add_to_file(str(dirc) + "|" + str(xx) + "," + str(yy))
        turtle.onscreenclick(dragging)

def upload():
    screen.reset()
    with open("draw_game_download", "r") as r:
        lines = r.readlines()
        t.forward(10)
        for lin in lines:
            linn = lin.split("\n")
            line = str(linn[0])
            if black in str(line):
                t.pencolor(black)
            elif blue in str(line):
                t.pencolor(blue)
            elif red in str(line):
                t.pencolor(red)
            elif green in str(line):
                t.pencolor(green)
            elif pink in str(line):
                t.pencolor(pink)
            elif "penup" in str(line):
                t.penup()
            elif "pendown" in str(line):
                t.pendown()
            elif "restart" in str(line):
                screen.reset()
                t.left(90)
            elif "z" in str(line):
                t.undo()
            elif "heart" in str(line):
                heart()
            elif "up" in str(line):
                up()
            elif "down" in str(line):
                down()
            elif "left" in str(line):
                left()
            elif "right" in str(line):
                right()
            try:
                fcor = line.split("|")
                cor = fcor[1].split(",")
                if fcor[1].count(",") != 1:
                    zzzzz  = 0 // 0
                else:
                    t.setheading(float(fcor[0]))
                    t.setposition(float(cor[0]),float(cor[1]))
            except:
                pass
            try:
                ww = int(line)
                t.width(ww)
            except:
                pass

def download():
    with open("draw_game_download", "w") as w:
        w.write("")
    with open("draw_game_download", "a") as a:
        for i in start_list:
            a.write(i + "\n")

screen.listen()
screen.onkeypress(control_z, "z")
screen.onkeypress(hide, "v")
screen.onkeypress(make_dot, "d")
screen.onkeypress(make_circle, "c")
screen.onkeypress(make_square, "s")
screen.onkeypress(right, "Right")
screen.onkeypress(up, "Up")
screen.onkeypress(left, "Left")
screen.onkeypress(down, "Down")
screen.onkeypress(heart, "h")

def main():
    turtle.listen()
    t.ondrag(dragging)
    screen.update()
    screen.mainloop()

main()