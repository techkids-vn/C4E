from turtle import *

for side in range(6,3,-1):
    for i in range(side):
        forward(100)
        left(360/side)
mainloop()