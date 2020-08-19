import rhinoscriptsyntax as rs
import random

def randomCurve(nPoints):
    coords = []
    for i in range(nPoints):
        v1 = i
        v2 = random.uniform(-100, 100)
        v3 = 0
        coords.append([v1, v2, v3])
    rs.AddInterpCurve(coords, 3)

for i in range(100):
    randomCurve(i+2)
