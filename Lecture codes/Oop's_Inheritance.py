#1.SINGLE INHERITANCE:-
'''
class A:             #class-A is parent class.     
    def getA(self,a):
        self.a = a      #self.a is a object of class-A.
    def putA(self):
        print("A: ",self.a)    
      
class B(A):          #class-B is inherited class of class-A. or child class.
    def getB(self,b):   #self.b is a object of class-B.
        self.b = b
    def putB(self):
        print("B: ",self.b)         
 
print("*********SINGLE INHERITANCE************")        
b1 = B()      #create one object b1 of class-B.
b1.getA(10)   #here access property of class-A using object of class-B.
b1.putA()
b1.getB(20)   #here access property of class-B using object of class-B.
b1.putB()    
'''

#2.MULTILEVEL INHERITANCE:-
'''
class A:             #class-A is parent class.     
    def getA(self,a):
        self.a = a      #self.a is a object of class-A.
    def putA(self):
        print("A: ",self.a)    
      
class B(A):          #class-B is inherited class of class-A. or child class.
    def getB(self,b):   #self.b is a object of class-B.
        self.b = b
    def putB(self):
        print("B: ",self.b)   
  
class C(B):          #class-C is inherited class of class-B. or child class of class-B and A.
    def getC(self,c):   #self.b is a object of class-B.
        self.c = c
    def putC(self):
        print("C: ",self.c)             
print("**********MULTILEVEL INHERITANCE************")        
c1 = C()      #create one object c1 of class-C.
c1.getA(10)   #here access property of class-A using object of class-C.
c1.putA()
c1.getB(20)   #here access property of class-B using object of class-C.
c1.putB()    
c1.getC(30)   #here access property of class-C using object of class-C.
c1.putC()   
'''
#3.MULTIPLE INHERITANCE:-
'''
class A:             #class-A is parent class.     
    def getA(self,a):
        self.a = a      #self.a is a object of class-A.
    def putA(self):
        print("A: ",self.a)    
      
class B:             #class-B is parent class.
    def getB(self,b):   #self.b is a object of class-B.
        self.b = b
    def putB(self):
        print("B: ",self.b)   
  
class C(A,B):          #class-C is inherited class of class-A and B. or child class of class-B and A.
    def getC(self,c):   #self.b is a object of class-B.
        self.c = c
    def putC(self):
        print("C: ",self.c)             

print("**********MULTIPLE INHERITANCE************")       
c1 = C()      #create one object c1 of class-C.
c1.getA(10)   #here access property of class-A using object of class-C.
c1.putA()
c1.getB(20)   #here access property of class-B using object of class-C.
c1.putB()    
c1.getC(30)   #here access property of class-C using object of class-C.
c1.putC()   
'''
#4.HIERARCHY INHERITANCE:-
'''
class A:             #class-A is parent class.     
    def getA(self,a):
        self.a = a      #self.a is a object of class-A.
    def putA(self):
        print("A: ",self.a)    
      
class B(A):             #class-B is inherited class of class-A.or child class of class-A.
    def getB(self,b):   #self.b is a object of class-B.
        self.b = b
    def putB(self):
        print("B: ",self.b)   
  
class C(A):          #class-C is inherited class of class-A.or child class of class-A.
    def getC(self,c):   #self.c is a object of class-C.
        self.c = c
    def putC(self):
        print("C: ",self.c) 
        
class D(A):          #class-D is inherited class of class-A.or child class of class-A.
    def getD(self,d):   #self.d is a object of class-D.
        self.d = d
    def putD(self):
        print("D: ",self.d)                    

print("**********HIERARCHY INHERITANCE************")       

b1 = B()        #create one object b1 of class-B.
c1 = C()        #create one object c1 of class-C.
d1 = D()        #create one object d1 of class-D.

b1.getA(10)     #property of class-A is access using class B,C and D.
b1.putA()       #if get fun is used from class-B than put fun is compulsory from class-B.

b1.getB(20)     #property of class-B is access using class B.
c1.getC(30)     #property of class-c is access using class c.
d1.getD(40)     #property of class-D is access using class D.
b1.putB()
c1.putC()
d1.putD()
'''
#5.HYBRID INHERITANCE:-  
# most inportant type of inheritance.one object(d1) access all parent class(class-A,B,C) properties.

class A:             #class-A is parent class.     
    def getA(self,a):
        self.a = a      #self.a is a object of class-A.
    def putA(self):
        print("A: ",self.a)    
      
class B(A):             #class-B is inherited class of class-A.or child class of class-A.
    def getB(self,b):   #self.b is a object of class-B.
        self.b = b
    def putB(self):
        print("B: ",self.b)   
  
class C(A):          #class-C is inherited class of class-A.or child class of class-A.
    def getC(self,c):   #self.c is a object of class-C.
        self.c = c
    def putC(self):
        print("C: ",self.c) 
        
class D(B,C):          #class-D is inherited class of class-B and C.or child class of class-A,B and C.
    def getD(self,d):   #self.d is a object of class-D.
        self.d = d
    def putD(self):
        print("D: ",self.d)                    

print("**********HYBRID INHERITANCE************")       

d1 = D()        #create one object d1 of class-D.

d1.getA(10)     #property of class-A is access using object of class-D.
d1.putA()       #if get fun is used from class-D than put fun is compulsory from class-D.

d1.getB(20)     #property of class-B is access using class-D.
d1.getC(30)     #property of class-c is access using class-D.
d1.getD(40)     #property of class-D is access using class-D.
d1.putB()
d1.putC()
d1.putD()




















