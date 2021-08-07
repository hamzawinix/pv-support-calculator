
import math as m

# angle = int(input("Enter angle : "))
# rows = int(input("Enter rows : "))

def degrees(rad):
    return rad * 180 / m.pi
def radians(deg):
    return deg * m.pi / 180



PVhight = 2
clamp = 0.038
angle = 27
rows = 2
panelPerRow = 5
panelWidth = 1
print ("angle :",angle)
theta = radians(angle)



# print (theta)
# print (m.tan(theta))

h1 = (2*0.1) + (0.4/2  * m.tan (theta)) 
rafter = rows * (PVhight+clamp ) - clamp
bracket = rafter * m.cos(theta) 
ax = bracket / 2
h2 = (ax * m.tan(theta)) + h1
h3 = (ax * m.tan(theta)) + h2

purlin = panelPerRow * (panelWidth + clamp) - clamp + 0.2
print ("H1 :",h1)
print ("H2 :",h2)
print ("H3 :",h3)
print ("purlin :",purlin)
print ("bracket :",bracket)
print ("ax :",ax)
print ("rafter :",rafter)

