from abc import ABC, abstractmethod

class Vehicle(ABC):      #parent class 
    @abstractmethod            #defined abstract method is compulsory.          
    def no_of_tyre(self,tyre):   #this parent class abstract method is defined in all child class.
        pass                     #this class fun is only declaration fun.
 
class Bullet(Vehicle):   #child class of Vehicle class. or abstracted class of Vehicle
    def no_of_tyre(self, tyre):
        self.tyre = tyre
        print("Bullet have",self.tyre,"tyres") 
 
class Auto(Vehicle):      #child class of Vehicle class. or abstracted class of Vehicle
    def no_of_tyre(self, tyre):
        self.tyre = tyre
        print("Auto have",self.tyre,"tyres")           
        
class Car(Vehicle):       #child class of Vehicle class. or abstracted class of Vehicle
    def no_of_tyre(self, tyre):
        self.tyre = tyre
        print("Car have",self.tyre,"tyres")        
        
bl = Bullet()
bl.no_of_tyre(2)        
at = Auto()
at.no_of_tyre(3)   
cr = Car()
cr.no_of_tyre(4)     
        