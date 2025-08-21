from turtle import Turtle

class TurtleName(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        self.color("black")
        self.penup()
        self.update_name(name, x, y)
        self.pendown()
        self.hideturtle()

    def update_name(self, name, x, y):
        self.goto(x, y)
        self.name = name
        self.clear()
        self.write(self.name, align="center", font=("Courier", 16, "normal"))
