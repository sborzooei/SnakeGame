from turtle import Turtle
ALIGHNMENT = "center"
FONT = ("Arial", 14, "normal")
FONT2 = ("Arial", 16, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("pink")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGHNMENT, font = FONT)


    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER", align=ALIGHNMENT, font=FONT2)



