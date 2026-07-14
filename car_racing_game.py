import turtle
import random
import time

# ============================
# WINDOW
# ============================
win = turtle.Screen()
win.title("Professional Car Racing")
win.bgcolor("darkgreen")
win.setup(width=700, height=800)
win.tracer(0)

# ============================
# GAME VARIABLES
# ============================
score = 5
high_score = 5
lives = 6
speed = 1
paused = False
day = True

# ============================
# ROAD
# ============================
road = turtle.Turtle()
road.hideturtle()
road.speed(0)
road.pensize(3)
road.color("white")
road.penup()

road.goto(-180,-400)
road.pendown()
road.goto(-180,400)

road.penup()
road.goto(180,-400)
road.pendown()
road.goto(180,400)

# ============================
# CENTER LINES
# ============================
lines=[]

for i in range(12):

    t=turtle.Turtle()

    t.speed(0)

    t.shape("square")

    t.color("white")

    t.shapesize(2,0.3)

    t.penup()

    t.goto(0,350-i*70)

    lines.append(t)

# ============================
# PLAYER CAR
# ============================
player=turtle.Turtle()

player.speed(0)

player.shape("square")

player.color("blue")

player.shapesize(2,1)

player.penup()

player.goto(0,-320)

# ============================
# ENEMIES
# ============================
enemies=[]

colors=["red","orange","yellow","purple"]

for i in range(5):

    e=turtle.Turtle()

    e.speed(0)

    e.shape("square")

    e.color(random.choice(colors))

    e.shapesize(2,1)

    e.penup()

    e.goto(random.choice([-120,-60,0,60,120]),
           random.randint(200,900))

    enemies.append(e)

# ============================
# COIN
# ============================
coin=turtle.Turtle()

coin.speed(0)

coin.shape("circle")

coin.color("gold")

coin.penup()

coin.goto(random.choice([-120,-60,0,60,120]),
          random.randint(300,700))

# ============================
# SCORE BOARD
# ============================
pen=turtle.Turtle()

pen.hideturtle()

pen.penup()

pen.color("white")

pen.goto(-330,350)

def update_board():

    pen.clear()

    pen.write(
        f"Score:{score}  Lives:{lives}  High:{high_score}",
        font=("Arial",16,"bold")
    )

update_board()

# ============================
# PLAYER MOVEMENT
# ============================
def left():

    x=player.xcor()

    if x>-100:

        player.setx(x-40)

def right():

    x=player.xcor()

    if x<100:

        player.setx(x+40)

win.listen()

win.onkeypress(left,"Left")

win.onkeypress(right,"Right")
# ============================
# POLICE CAR
# ============================
police = turtle.Turtle()
police.speed(0)
police.shape("square")
police.color("black")
police.shapesize(2,1)
police.penup()
police.goto(60,600)

# ============================
# TRUCK
# ============================
truck = turtle.Turtle()
truck.speed(0)
truck.shape("square")
truck.color("brown")
truck.shapesize(3,2)
truck.penup()
truck.goto(-60,800)

# ============================
# PAUSE
# ============================
def pause_game():
    global paused
    paused = not paused

win.onkeypress(pause_game,"p")
win.onkeypress(pause_game,"P")

# ============================
# DAY / NIGHT MODE
# ============================
def change_mode():

    global day

    if day:
        win.bgcolor("black")
        pen.color("yellow")
        day=False
    else:
        win.bgcolor("darkgreen")
        pen.color("white")
        day=True

win.onkeypress(change_mode,"d")
win.onkeypress(change_mode,"D")

# ============================
# RESTART
# ============================
def restart():

    global score
    global lives
    global speed

    score = 5
    lives = 2
    speed = 1

    player.goto(0, -320)

    for enemy in enemies:
        enemy.goto(
            random.choice([-120, -60, 0, 60, 120]),
            random.randint(400, 900)
        )

    police.goto(60, 600)

    truck.goto(-60, 800)

    coin.goto(
        random.choice([-120, -60, 0, 60, 120]),
        random.randint(400, 700)
    )

    update_board()

win.onkeypress(restart, "r")
win.onkeypress(restart, "R")

# ============================
# MAIN LOOP
# ============================
while True:

    win.update()

    if paused:
        time.sleep(0.1)
        continue

    # Road Animation
    for line in lines:

        line.sety(line.ycor()-speed)

        if line.ycor()<-420:
            line.sety(420)

    # Enemy Cars
    for enemy in enemies:

        enemy.sety(enemy.ycor()-speed)

        if enemy.ycor()<-420:

            enemy.goto(
                random.choice([-120,-60,0,60,120]),
                random.randint(450,900)
            )

            score += 1

            if score % 20 == 0:
             speed += 0.2

            update_board()

        # Collision
        if player.distance(enemy)<30:

            lives -=1

            update_board()

            enemy.goto(
                random.choice([-120,-60,0,60,120]),
                700
            )

            if lives<=0:

                pen.goto(-120,0)

                pen.write(
                    "GAME OVER",
                    font=("Arial",30,"bold")
                )

                win.update()

                break
            # ============================
# COIN MOVEMENT
# ============================

    coin.sety(coin.ycor() - speed)

    if coin.ycor() < -420:

        coin.goto(
            random.choice([-120,-60,0,60,120]),
            random.randint(450,900)
        )

    if player.distance(coin) < 20:

        score += 5

        if score > high_score:
            high_score = score

        update_board()

        coin.goto(
            random.choice([-120,-60,0,60,120]),
            random.randint(450,900)
        )

# ============================
# POLICE MOVEMENT
# ============================

    police.sety(police.ycor() - (speed + 1))

    if police.ycor() < -200:

        police.goto(
            random.choice([-120,-60,0,60,120]),
            random.randint(600,900)
        )

    if player.distance(police) < 30:

        lives -= 1

        update_board()

        police.goto(
            random.choice([-120,-60,0,60,120]),
            1000
        )

# ============================
# TRUCK MOVEMENT
# ============================

    truck.sety(truck.ycor() - (speed - 1))

    if truck.ycor() < -450:

        truck.goto(
            random.choice([-120,-60,0,60,120]),
            random.randint(900,1000)
        )

    if player.distance(truck) < 40:

        lives -= 1

        update_board()

        truck.goto(
            random.choice([-120,-60,0,60,120]),
            1400
        )

# ============================
# GAME OVER CHECK
# ============================

    if lives <= 0:

        pen.clear()

        pen.goto(-150,40)

        pen.color("red")

        pen.write(
            "GAME OVER",
            font=("Arial",32,"bold")
        )

        pen.goto(-140,-20)

        pen.color("white")

        pen.write(
            f"Final Score : {score}",
            font=("Arial",20,"bold")
        )

        pen.goto(-180,-70)

        pen.write(
            "Press R To Restart",
            font=("Arial",18,"bold")
        )

        win.update()

        while lives <= 0:

            win.update()
            time.sleep(0.02)

# ============================
# END
# ============================

win.mainloop()