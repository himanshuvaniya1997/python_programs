#object oriented program for make calculator.

class Calculator:      
    
    def sum(self,num1,num2):
        self.a = num1
        self.b = num2
        self.c = self.a + self.b
        print(self.c)
    def sub(self,num1,num2):
        self.a = num1
        self.b = num2
        self.c = self.a - self.b   
        print(self.c)
    def mul(self,num1,num2):
        self.a = num1
        self.b = num2
        self.c = self.a * self.b
        print(self.c)
    def div(self,num1,num2):
        self.a = num1
        self.b = num2
        self.c = self.a / self.b 
        print(self.c)     
        
cal = Calculator()

while True:
    print("1. sum")
    print("2. sub")
    print("3. mul")
    print("4. div")
    print("5. exit")
    print("*"*80)
    
    choice = int(input("Enter Your Choice: ")) 
    if choice == 1:
        try:
            num1 = int(input("enter the num1: "))
            num2 = int(input("enter the num2: "))    
            cal.sum(num1, num2)
            print("*"*80)
        except Exception as e:
            print("Exception occur: ",e)    
    elif choice == 2:
        try:
            num1 = int(input("enter the num1: "))
            num2 = int(input("enter the num2: "))
            cal.sub(num1, num2)
            print("*"*80)
        except Exception as e:
            print("Exception occur: ",e)  
    elif choice == 3:
        try:
            num1 = int(input("enter the num1: "))
            num2 = int(input("enter the num2: "))
            cal.mul(num1, num2)
            print("*"*80)
        except Exception as e:
            print("Exception occur: ",e)    
    elif choice == 4:
        try:
            num1 = int(input("enter the num1: "))
            num2 = int(input("enter the num2: "))
            cal.div(num1, num2)
            print("*"*80)
        except Exception as e:
            print("Exception occur: ",e)    
    elif choice == 5:
        exit()
    else:
        print("THANKS FOR VISIT CALCULATOR")
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
           