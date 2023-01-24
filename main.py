from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# Screen adjustments
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating objects of external classes
downy = Player()
car = CarManager()
scoreboard = Scoreboard()

# Adjusting screen for listening on key click
screen.listen()
# DON'T use parenthesis () after a function inside the onkey() function
screen.onkey(fun=downy.up, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.generator()
    car.move_cars()

    # Detect collision with car
    for sample_car in car.cars:

        if sample_car.distance(downy) < 28:
            scoreboard.game_over()
            game_is_on = False

    # Detect Successful road passing
    if downy.reset():
        car.accelerate()
        scoreboard.increase_level()

screen.exitonclick()
