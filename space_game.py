import turtle
import winsound
import math
import random

# creating the screen
sc = turtle.getscreen()
sc.bgcolor("black")
# sc.screensize(1000, 1000)
sc.title("Space Invaders")
sc.bgpic("background.gif")
sc.tracer(0)
sc.register_shape("player.gif")
sc.register_shape("invaders.gif")

# creating the border
b_pen = turtle.Turtle()
b_pen.speed(0)
b_pen.color("white")
b_pen.pensize(3)
b_pen.penup()
b_pen.setposition(-330, -320)
b_pen.pendown()
for i in range(4):
    b_pen.fd(640)
    b_pen.lt(90)
b_pen.hideturtle()

# creating score
score = 0
score_pen = turtle.Turtle()
score_pen.color("white")
score_pen.speed(0)
score_pen.penup()
score_pen.hideturtle()
score_pen.setposition(-320, 295)
scorestring = "Score: {0}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

# creating the player
player = turtle.Turtle()
player.speed(0)
player.shape("player.gif")
player.lt(90)
player.color("blue")
player.turtlesize(1)
player.penup()
player.setposition(-1, -250)
player.speed = 0

# creating multiple enemies using lists
no_of_enemies = 10
enemies = []
for i in range(no_of_enemies):
    # creating the enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.speed(0)
    enemy.color("red")
    enemy.shape("invaders.gif")
    enemy.penup()
    x = random.randint(-290, 310)
    y = random.randint(100, 290)
    enemy.setposition(x, y)
    enemy.turtlesize(0.8)

enemyspeed = 0.4

# creating the players bullet
bullet = turtle.Turtle()
bullet.speed(0)
bullet.penup()
bullet.hideturtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.lt(90)
bullet.shapesize(0.4, 0.4)
bullet.setposition(0, -250)

bulletspeed = 6
# bulletstate = ready or firing
bulletstate = "ready"


# func to move left
def move_lft():
    player.speed = -2


# func to move right
def move_rgt():
    player.speed = 2


def move_player():
    x = player.xcor()
    x += player.speed
    if x < -300:
        x = -300
    if x > 280:
        x = 280
    player.setx(x)


def fire_bull():
    # global bulletstate so changes can be reflected outside the func def
    global bulletstate
    # initial position of bullet
    if bulletstate == "ready":
        winsound.PlaySound("bullet_sound.wav", winsound.SND_ASYNC)
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 25:
        return True
    else:
        return False


# keyboard listener
sc.listen()
sc.onkeypress(move_lft, 'Left')
sc.onkeypress(move_rgt, 'Right')
sc.onkey(fire_bull, "space")

while True:
    sc.update()
    move_player()
    for enemy in enemies:
        # keep moving the enemy through the game
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # to move enemy downwards
        if x > 290:
            # move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            enemyspeed *= -1

        if x < -310:
            # move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            enemyspeed *= -1

        # hitting the enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            bullet.hideturtle()
            bulletstate = "ready"
            enemy.setposition(0, 400)
            bullet.setposition(0, -500)
            # update score
            score += 10
            scorestring = "Score: {0}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        # enemy killing player
        if isCollision(player, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    # move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # changing bullet state
    if bullet.ycor() > 330:
        bullet.hideturtle()
        bulletstate = "ready"

# sc.mainloop()
# delay = input("press enter to exit")
