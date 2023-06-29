#method overloading.(not supported by python)
#problem:- access only last fun in same class.
'''
class point:   
    
    def test(self):
        print("test with no arguments")
    def test(self,a):
        print("test with one arguments")
    def test(self,a,b): #last format of fun is override on all fun.so only last fun format is called.
        print("test with two arguments")    
        
obj = point()
obj.test(10,20)        
'''        
#Operator overloading.(supported by python)
#solution:- access any funtion in same class using different operators(Magic method).

class Point:
    def __init__(self):   #init call automatically when object is created.
        print("init called")            
p1 = Point() 

class Point1:
    def __init__(self,a,b):   #init call automatically when object is created.
            self.a = a
            self.b = b
            print("init called for second time") 
            
    def __str__(self):  #str call automatically when print the object.
        print("str called")  
        return  "({0},{1})".format(self.a,self.b)   #return a string is compulsory. 
      
    def __add__(self,obj):   #add call automatically when addition operation called.
        print("Add called")
        a = self.a + obj.a
        b = self.b + obj.b
        return P(a, b)
    def __sub__(self,obj):
        print("SUB called")
        a = self.a - obj.a
        b = self.b - obj.b
        return P(a, b)
        
    
p2 = P(10, 20)  #if argument given in init fun then compulsory to give argument at call time.
print(p2)     #__str__ called.
p3 = P(20, 30)
print(p3)     #__str__ called.
print("Addition of 2 objects: ",p2+p3) #p2=self and p3=obj in def __add__.  
print(type(p2+p3))
print("Addition of 2 objects: ",p2-p3)


  

       
        