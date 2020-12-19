
'''
Sample pong game using python 
    -  with out using oop (old School)
    - no need  to download modules
'''

import turtle  
# _____________window settings___________#
wn = turtle.Screen()
wn.title("pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # stops the window from updating && speed up our game

# _______________ Score ________________#
score_a = 0
score_b = 0
# __________________ objects _________________#
# Paddle A
paddle_a = turtle.Turtle() 
paddle_a.speed(0) # maximum speed for all objects animation speed
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # dissable drowing lines
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.3  # every time move by 2px
ball.dy = -0.3

# Pen
pen = turtle.Turtle()
pen.speed(0) 
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A: 0  Player B : 0' , align='center',font=('courier', 24 ,'normal'))

# _____________functions to move paddels using keyboards_____________#
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# _____________keyboard  binding  to call function____________#
wn.listen()
wn.onkeypress(paddle_a_up,'u')
wn.onkeypress(paddle_a_down,'d')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')

# ___________Main game loop____________#
while True:
    wn.update()
    #move the ball
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # border checking
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390 :
        ball.goto(0,0)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B : {score_b}', align='center', font=('courier', 24, 'normal'))
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B : {score_b}', align='center', font=('courier', 24, 'normal'))

        # paddle and ball collision
        
    if (ball.xcor() > 340 and ball.xcor() < 350)  and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 ):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350)  and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40 ):
        ball.setx(-340)
        ball.dx *= -1
