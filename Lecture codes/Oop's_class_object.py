class Student:           #create class with its name Student.
    
    test = "pass"
    
    def getData(self,fname,lname):   #create fun in class.self argument compulsory in every fun.
        self.f = fname
        self.l = lname
    def putData(self):               #create fun in class
        print("first name: ",self.f)    
        print("last name: ",self.l)    
       
s1 = Student()           #here s1 is object for class Student.
s2 = Student()

s1.getData("Himanshu","Vaniya") #in getData fun self = s1.
s1.putData()                #in putData fun self = s1.    

#different class objects have a different Memory Locations.
print("Address or Memory location of object s1: ",s1)   
print("Address or Memory location of object s2: ",s2)

print(Student.test)   #so here test is a variable of class Student.