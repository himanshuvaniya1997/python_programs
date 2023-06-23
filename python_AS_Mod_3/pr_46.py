#WAP to calculate the area of a parallelogram.

def area_of_parallelogram(base,height):
    return base * height

base = int(input("Enter the base length: "))
height = int(input("Enter the height: "))
print(area_of_parallelogram(base, height),"square units")
