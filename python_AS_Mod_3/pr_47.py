#WAP to calculate surface volume and area of a cylinder.

pi = 3.14
def cylin_area(r,h):
    return 2*pi*(r*r) + 2*pi*r*h
def cylin_volume(r,h):
    return pi*(r*r)*h

radius = 5
height = 10
area = cylin_area(radius, height)
volume = cylin_volume(radius,height)

print("Area of cylinder: ",area,"square units")
print("Volume of cylinder: ",volume,"square units")
print("Area of cylinder in pi:",area/3.14,"π")
print("Volume of cylinder in pi:",volume/3.14,"π")
