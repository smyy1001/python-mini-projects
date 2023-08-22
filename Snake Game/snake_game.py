"""
author: sumeyye acar
date: 8-21-2023
file: snake_game.py
"""

# if the libraries aren't present in you system type in terminal (without the quotation marks and brackets): 
# "pip install [library-name]"

# importing needed libraries
import random
import time
import turtle


# initial score adjustment
score = 0
delay = 0.1


# building up the tutle screen
snake_game_screen = turtle.Screen()
snake_game_screen.setup( width = 700, height = 700 )
snake_game_screen.title( "SNAKE GAME" )
turtle.bgcolor( 'light green' )
snake_game_screen.tracer(0)


# setting the game borders
turtle.speed(5)
turtle.pensize(5)
turtle.penup() # leave no trace behind (as in actual drawing)
turtle.goto(-310,250)
turtle.pendown() # leave traces (as in actual drawing)
turtle.color('white')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()


# snake 
snake = turtle.Turtle()
snake.speed(0)
snake.shape( "square" )
snake.color( 'red' )
snake.penup()
snake.goto( 0, 0 )
snake.direction = 'stop'


# snake food
food = turtle.Turtle()
food.speed(0)
food.shape( "circle" )
food.color( 'blue' )
food.penup()
food.goto( 20, 70 )
eaten_food= []


# scor handeling
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color( "black" )
scoring.penup()
scoring.hideturtle()
scoring.goto( 0, 300 )
scoring.write( "Score: ", align= "center", font= ( "Courier", 20, "bold" ) )


# movement definition
const_speed = 15

def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def move():
    y = snake.ycor()
    x = snake.xcor()

    if snake.direction == "up":
        snake.sety( y + const_speed )
    if snake.direction == "down":
        snake.sety( y - const_speed )
    if snake.direction == "left":
        snake.setx( x - const_speed )
    if snake.direction == "right":
        snake.setx( x + const_speed )


# keyboard commands
snake_game_screen.listen()
snake_game_screen.onkeypress( go_up, "Up" )
snake_game_screen.onkeypress( go_down, "Down" )
snake_game_screen.onkeypress( go_left, "Left" )
snake_game_screen.onkeypress( go_right, "Right" )


# main game!
while True:
    snake_game_screen.update()

    # snake reaching the food
    if snake.distance(food) < const_speed:
        x = random.randint( -290, 270 )
        y = random.randint( -240, 240 )
        food.goto( x, y )
        scoring.clear()
        score += 1
        scoring.write( "Score: {}".format( score ), align="center", font=( "Courier", 20, "bold" ) )
        delay -= 0.001

        # adding food
        next_food = turtle.Turtle()
        next_food.speed(0)
        next_food.shape( 'square' )
        next_food.color( 'blue' )
        next_food.penup()
        eaten_food.append( next_food )

    # lengthening the snake
    for i in range( len(eaten_food)-1, 0, -1 ):
        temp_x = eaten_food[i-1].xcor()
        temp_y = eaten_food[i-1].ycor()

        eaten_food[i].goto( temp_x, temp_y )

    if len( eaten_food ) > 0:
        temp_x2 = snake.xcor()
        temp_y2 = snake.ycor()
        eaten_food[0].goto( temp_x2, temp_y2 )
    
    move()

    #snake reaching the border walls
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        snake_game_screen.clear()
        snake_game_screen.bgcolor( 'light green' )
        scoring.goto( 0, 0 ) 
        scoring.write( "GAME OVER \nYour Score is {}".format(score), align="center", font=( "Courier", 28, "bold" ) )


    # snake biting itself
    for f in eaten_food:
        if f.distance( snake ) < const_speed:
            time.sleep(1)
            snake_game_screen.clear()
            snake_game_screen.bgcolor( 'light green' )
            scoring.goto( 0, 0 )
            scoring.write( "GAME OVER \nYour Score is {}".format(score), align="center", font=( "Courier", 28, "bold" ) )


    time.sleep(delay)

turtle.Terminator()
