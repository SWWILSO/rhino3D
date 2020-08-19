import rhinoscriptsyntax as rs
import random

origin = (0, 0, 0)

for i in range(100000):
    x = random.uniform(-100, 100)
    y = random.uniform(-100, 100)
    z = random.uniform(-100, 100)
    coord = (x, y, z)
    
    if rs.Distance(coord, origin) > 90 and rs.Distance(coord, origin) < 95:
        rs.AddPoint(coord)
