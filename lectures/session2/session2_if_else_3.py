from turtle import *

color("black", "white")

for side in range(5, 2, -1):
    if side == 3:
        color("blue", "green")
    elif side == 4:
        color("purple", "yellow")
    else:
        color("red", "pink")
    begin_fill()
    for i in range(side):
        forward(100)
        left(360/side)
    end_fill()
mainloop()
