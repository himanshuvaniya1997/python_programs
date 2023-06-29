#Basic code for method overriding.
#problem:- In this code not possible to access proprties of base class.so solution in next code. 
'''
class A:       #base class
    def show(self):             #same method or fun in both class.
        print("Show from Class A")
        
class B(A):    #derived class    
    def show(self):             #same method or fun in both class.
        print("Show from Class B")        
        
b1 = B()    #create object of derived class B.
b1.show()        
'''       
#Problem solving code for method overriding using super function.

#1.Single Inheritance.
'''
class A:       #base class
    def show(self):             #same method or fun in both class.
        print("Show from Class A")
        
class B(A):    #derived class of A   
    def show(self):             #same method or fun in both class.
        super().show()          #used super() fun for access property of base class.
        print("Show from Class B")                
 
b1 = B()    #create object of derived class B.
b1.show()           
'''           
#2.Multilevel Inheritance.
'''
class A:       #base class
    def show(self):             #same method or fun in all class.
        print("Show from Class A")
        
class B(A):    #derived class of A   
    def show(self):             #same method or fun in all class.
        super().show()          #used super() fun for access property of base class A.
        print("Show from Class B")                  

class C(B):    #derived class of B  
    def show(self):             #same method or fun in all class.
        super().show()          #used super() fun for access property of base class B.
        print("Show from Class C")         
        
c1 = C()   #Create object of Class-C.
c1.show()       
'''        
#3.Multiple Inheritance.
'''
class A:       #base class
    def show(self):             #same method or fun in all class.
        print("Show from Class A")
        
class B:       #base class.   
    def show(self):             #same method or fun in all class.
        super().show()
        print("Show from Class B")                  

class C(B,A):    #derived class of B and A.  In multiple Inheritance always base class in reverse order.
    def show(self):             #same method or fun in all class.
        super().show()       
        print("Show from Class C")         
        
c1 = C()   #Create object of Class-C.
c1.show()               
'''

#4.Hierarchy Inheritance.
'''
class A:       #base class
    def show(self):             #same method or fun in all class.
        print("Show from Class A")
        
class B(A):       #derived class of A.   
    def show(self):             #same method or fun in all class.
        super().show()          #call super fun for access property of class A.
        print("Show from Class B")                  

class C(A):       #derived class of A.
    def show(self):             #same method or fun in all class.      
        print("Show from Class C")         

class D(A):       #derived class of A.
    def show(self):             #same method or fun in all class.
    
        print("Show from Class D")   

b1 = B()   #Create object of Class-B.             
c1 = C()   #Create object of Class-C.
d1 = D()   #Create object of Class-D.

b1.show()
c1.show()           
d1.show()
'''
#5.Hybrid Inheritance.
'''
class A:       #base class
    def show(self):             #same method or fun in all class.
        print("Show from Class A")
        
class B(A):       #derived class of A.   
    def show(self):             #same method or fun in all class.
        super().show()
        print("Show from Class B")                  

class C(A):       #derived class of A.
    def show(self):             #same method or fun in all class.      
        super().show()          
        print("Show from Class C")         

class D(C,B):       #derived class of C and B.
    def show(self):             #same method or fun in all class.
        super().show()          #first called C and after B.
        print("Show from Class D") 

d1 = D()
d1.show()
'''
        