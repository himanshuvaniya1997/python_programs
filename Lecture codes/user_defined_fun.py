#1.function with no arguments & no return value.

def printline():
    print("*"*50)
   
printline()
print("welcome to UDF in pyhton.") 
printline()   

#2.function with arguments but no return value.

def add(a,b):
    print("Addition: ",a+b)
  
printline() 
x = int(input("enter value x: ")) 
y = int(input("enter value y: ")) 
add(x,y) 
printline()

#3.function with arguments and return value.

def sub(a,b):
    return a-b

printline()
x = int(input("enter value x: ")) 
y = int(input("enter value y: ")) 
ans = sub(x,y)
print("Subtraction: ",ans)
printline()








    