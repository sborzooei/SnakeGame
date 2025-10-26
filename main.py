from turtle import Screen, Turtle
from snakeclass import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()

screen.setup(width = 600, height = 600)

screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

mySnake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(mySnake.up,"Up")
screen.onkey(mySnake.down,"Down")
screen.onkey(mySnake.left,"Left")
screen.onkey(mySnake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    mySnake.move()

    # Detect collision with food.
    if mySnake.head.distance(food)<15:
        food.refresh()
        mySnake.extend()
        score.increase_score()


    #Detect collision with wall
    if mySnake.head.xcor() > 300 or mySnake.head.xcor() <-300 or mySnake.head.ycor() >300 or mySnake.head.ycor() < -300:
        game_is_on = False
        score.game_over()

    #Detect collision with tail
    #if head collide with any other segment: trigger gameover
    for segment in mySnake.segments[1:]:
        if mySnake.head.distance(segment) <10:
            game_is_on = False
            score.game_over()





screen.exitonclick()