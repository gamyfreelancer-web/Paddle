from turtle import Turtle
import random
class turtle_shapes(Turtle):
    def __init__(self):
        super().__init__()
        self.list_turule=['arrow', 'turtle', 'circle', 'square', 'triangle']
        self.colerr=["red","green","blue","white"]
        self.x=random.randint(-380,380)
        self.y=320
        self.penup()
        self.goto(self.x,self.y)
    def falling(self):
        self.choice=random.choice(self.list_turule)
        if self.ycor()>-300:
            self.goto(self.x,self.ycor()-10)
            
            
 
      