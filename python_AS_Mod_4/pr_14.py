#write a python class named Circle constructed by a radius
#and two methods which will compute the area and the perimeter of a circle.

class Circle():
    
    def area_of_circle(self,radius):
        self.radius = radius
        return 3.14 * (self.radius **2)
    def perimeter_of_circle(self,radius):
        self.radius = radius
        return 2 * 3.14 * self.radius

obj = Circle()
area = obj.area_of_circle(5) 
perimeter = obj.perimeter_of_circle(5)   
print("Area of Circle: ",area)    
print("Perimeter of Circle: ",perimeter)    
