"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

Equipo:
- Julieta Aceves
- Fernando Santoyo
- Luis Karam
"""

from random import randrange
from turtle import *
from freegames import vector
import random

##to change ball and target colors randomly
color_range =['cyan', 'purple','black','red','green','blue']
ball_color = random.choice(color_range)
target_color= random.choice(color_range)
if target_color == ball_color:
	target_color = random.choice(color_range)

#Declaracion de variables 
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#Funcion para detectar clicks
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25
	if score > 3
		speed.x = (x + 200) / 20
	        speed.y = (y + 200) / 20

#Funcion para detectar si esta dentro de la pantalla
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

#Funcion para dibujar los objetos
def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, target_color)

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, ball_color)

    update()

#Funcion para definir como se va a mover el objeto
def move():
    "Move ball and targets."
    # Generate a new target at random times
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Move the existing targets
    for target in targets:
        target.x -= 0.5

    # Move the cannon shot
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    # Make a copy of the existing target list before redrawing
    dupe = targets.copy()
    targets.clear()

    # Detect if the bullet hits a target
    while:
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
	score=0
		score+=1
		print (score)
    draw()

    # Detect when a target reaches the left side
    for target in targets:
        if not inside(target):
            #Return targets to initial position in x
            target.x= 200

    ontimer(move, 50)

#Ejecucion
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
