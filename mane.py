from turtle import Turtle,Screen
from shapes import turtle_shapes
from paddel import _Paddel
import time

window=Screen()
window.bgcolor("black")
window.setup(800,600)
paddel=_Paddel()
window.listen()
window.onkey(paddel.right,"Right")
window.onkey(paddel.left,"Left")
shapes=turtle_shapes()
game_on=True
while game_on:   
    shapes.falling() 
    
   
    

window.exitonclick()

