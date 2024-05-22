# import packages
import turtle
import random
import time

# create screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# creating border
border = turtle.Turtle()
border.speed(5)
border.pensize(4)
border.penup()
border.goto(-310, 250)
border.pendown()
border.color("red")
border.forward(500)
border.right(90)
border.forward(500)
border.right(90)
border.forward(500)
border.right(90)
border.forward(500)
border.penup()
border.hideturtle()

# score
score = 0
delay = 0.1

# snake
snake = turtle.Turtle()
snake.speed(0)  # Set speed to the maximum
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

# scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: 0", align="center", font=("courier", 24, "bold"))

# define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# keyboard binding
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# main loop
while True:
    screen.update()

    # snake and fruit collision
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score: {}".format(score), align="center", font=("courier", 24, "bold"))
        delay -= 0.001

        # creating new food
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # move the end segments first in reverse order
    for index in range(len(old_fruit)-1, 0, -1):
        x = old_fruit[index-1].xcor()
        y = old_fruit[index-1].ycor()
        old_fruit[index].goto(x, y)

    # move segment 0 to where the head is
    if len(old_fruit) > 0:
        x = snake.xcor()
        y = snake.ycor()
        old_fruit[0].goto(x, y)

    snake_move()

    # check for collision with border
    if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write("   Game Over \n Your score is: {}".format(score), align="center", font=("courier", 30, "bold"))
        break  # Exit the main loop

    # check for collision with itself
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write("   Game Over \n Your score is: {}".format(score), align="center", font=("courier", 30, "bold"))
            break  # Exit the main loop

    time.sleep(delay)

turtle.done()
