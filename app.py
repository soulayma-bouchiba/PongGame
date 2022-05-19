#imported turtle module (turtle t5alini nsawir 7ajet 3al ecran w n5aliha tit7arik)
import turtle
#ecran mta3 game
wind = turtle.Screen()#intialize screen
wind.title("Ping Pong")#set the title of the game
wind.bgcolor("black")#set the background color of the game
wind.setup(width=800, height=600)#set the width and height of the game
wind.tracer(0)#stops the window from updating automatically

#madhrib1
madhrib1 = turtle.Turtle()#intialize turtle object(shape)
madhrib1.speed(0) #set the speed of the animation
madhrib1.shape("square")#set the shape of the object
madhrib1.color("blue")#set the color of the shape
madhrib1.shapesize(stretch_wid=5,stretch_len=1)#stretches the shape to shape to meet the size
madhrib1.penup()#stops the object from drawing lines
madhrib1.goto(-350,0)#set the position of the object

#madhrib2
madhrib2 = turtle.Turtle()
madhrib2.speed(0) 
madhrib2.shape("square")
madhrib2.color("red")
madhrib2.shapesize(stretch_wid=5,stretch_len=1)
madhrib2.penup()
madhrib2.goto(350,0)


#ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.4
ball.dy = 0.4

#Score
score1 =0
score2 =0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1: 0 Player 2: 0",align="center",font=("courier",24,"normal"))
#functions
def madhrib1_up():
   y = madhrib1.ycor()#get the y coordinate of the madhrib1
   y +=20 #set the y to increase be 20
   madhrib1.sety(y) #set the y of the madhrib1 to the new y coordinate

def madhrib1_down():
   y = madhrib1.ycor()
   y -=20 #set the y to decrease be 20
   madhrib1.sety(y)

def madhrib2_up():
       y = madhrib2.ycor()
       y +=20
       madhrib2.sety(y)

def madhrib2_down():
   y = madhrib2.ycor()
   y -=20
   madhrib2.sety(y)

#keybord bindings
wind.listen() #tell the window to expect keybord input 
wind.onkeypress(madhrib1_up,"Right") #when pressing w the function madhr00000000ib1_up is invoked
wind.onkeypress(madhrib1_down,"Left")

wind.onkeypress(madhrib2_up,"Up")
wind.onkeypress(madhrib2_down,"Down")


#main game loop
while True:
    wind.update() #update the screen everytime the loop run
    
    #move the ball
    ball.setx(ball.xcor()+ball.dx) #ball starts at 0 and everytime loops run --->+0.5 xaxis
    ball.sety(ball.ycor()+ball.dy)#ball starts at 0 and everytime loops run --->+0.5 yaxis
    #border check , top border +300px,bottom border -300px, ball is 20px
    if ball.ycor()>290: #if ball is at top border
        ball.sety(290) #set y coordinate +290
        ball.dy *= -1 #reverse direction, marking +0.5-->0.5

    if ball.ycor()<-290:#if ball is at bottom border
        ball.sety(-290)
        ball.dy *= -1    

    if ball.xcor()>390:#if ball is at right border
            ball.goto(0,0)#return ball center
            ball.dx *= -1 #reverse the x direction 
            score1 += 1
            score.clear()
            score.write("Player 1: {} Player 2: {}".format(score1,score2),align="center",font=("courier",24,"normal"))

    if ball.xcor()<-390: #if ball is at left border
            ball.goto(0,0)
            ball.dx *= -1
            score2 +=1
            score.clear()
            score.write("Player 1: {} Player 2: {}".format(score1,score2),align="center",font=("courier",24,"normal"))

    #tasadim madhrib and ball
    if(ball.xcor()>340 and ball.xcor()<350)and(ball.ycor()<madhrib2.ycor()+40 and ball.ycor()>madhrib2.ycor()-40):
        ball.setx(340)
        ball.dx*= -1       
    
    if(ball.xcor()<-340 and ball.xcor()>-350)and(ball.ycor()<madhrib1.ycor()+40 and ball.ycor()>madhrib1.ycor()-40):
        ball.setx(-340)
        ball.dx*= -1 

        