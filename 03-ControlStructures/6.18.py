'''
Let x and y denote the coordinates of a point on the plane. Write a program that determines
in which quadrant of the coordinate system the point P(x, y) is located or on which axis it
is located, or that it is located in the position (0,0) of the coordinate system. Sample result:

x = 5
y = 2
Point P(5,2) is in the first quadrant of the coordinate system
'''

x=0
y=1

if x > 0 and y > 0:
    quadrant='first quadrant'
elif x > 0 and y<0:
    quadrant='fourth quadrant'
elif x<0 and y>0:
    quadrant='second quadrant'
elif x<0 and y<0:
    quadrant='third quadrant'
elif x==0 and y==0:
    quadrant='center'
elif x==0:
    quadrant="x-axis"
elif y==0:
    quadrant="y-axis"


print(f'point p({x}:{y}) is located in the {quadrant} in the coordinate system')