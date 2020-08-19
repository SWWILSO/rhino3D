import rhinoscriptsyntax as rs
import random
import math

z = -100
radius = 0
theta = 0
i = 0

while z <= 100:
    if i % 4 == 0:
        x = (radius + 2) * math.cos(theta)
        y = (radius + 2) * math.sin(theta)
    else:
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

    rs.AddPoint((x,y,z))

    radius += .003
    theta += 1
    z += .01
    i += 1
