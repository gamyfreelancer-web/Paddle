from turtle import Turtle
class _Paddel(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0,-280)
        self.shapesize(1,10)
        
    def right(self):
        self.goto(self.xcor()+50,-280)
        
    def left(self):
        self.goto(self.xcor()-50,-280)       
        