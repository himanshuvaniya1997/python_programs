#write a python class named Rectangle constructed by a length and width.
#and a method which will compute the area of a rectangle.

class Rectangle():
    
    def area_of_recta(self,length,width):
        self.length = length
        self.width = width
        return self.length * self.width

obj = Rectangle()
area = obj.area_of_recta(20, 10)    
print("Area of Rectangle: ",area)    
