from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.penup()
        self.color('white')
        self.goto(-280, 250)
        self.update_scoreboard()

# Updates scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Level: {self.level}', align='left', font=FONT)

# Increases level number on a scoreboard
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

# Shows GAME OVER text when a player and car objects collide
    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align='center', font=FONT)


