from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.color('yellow')
        self.goto(STARTING_POSITION)

# Moves the player object up, to north
    def up(self):
        # Another way of moving the object
        # y = self.ycor() + MOVE_DISTANCE
        # self.goto(x=0, y=y)
        self.forward(MOVE_DISTANCE)

# Resets a player to its initial position and returns TRUE value
    def reset(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True



