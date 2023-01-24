from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.ht()

# Generates new car objects
    def generator(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randrange(-250, 250, 40)
            new_car.goto(y=random_y, x=310)
            self.cars.append(new_car)

# Moves car alongside X axis
    def move_cars(self):
        for car in reversed(self.cars):
            # The code below is another way of moving Car object
            # car.setx(car.xcor() - STARTING_MOVE_DISTANCE)
            if car.distance(self.cars[-1]) > 50:
                car.backward(self.car_speed)

# Increases the speed of cars
    def accelerate(self):
        self.car_speed += MOVE_INCREMENT

