import rhinoscriptsyntax as rs
import random

def randomCurve(nPoints):
    coords = []
    for i in range(nPoints):
        v1 = random.uniform(-100, 100)
        v2 = random.uniform(-100, 100)
        v3 = random.uniform(-100, 100)
        coords.append([v1, v2, v3])
    rs.AddInterpCurve(coords, 3)

curves = input("Enter number of curves: ")
for i in range(curves):
    randomCurve(i+2)
