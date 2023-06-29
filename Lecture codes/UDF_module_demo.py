import UDF    #user defined library.
 
while True:
    print("*"*50)
    print("1. oddeven") 
    print("2. maxoftwo") 
    print("3. maxofthree") 
    print("4. prime") 
    print("5. fibonacci") 
    print("6. exit")
    
    choice = int(input("Enter Your Choice: "))
    
    if choice == 1:
        n = int(input("enter n: "))
        print("*"*50)
        UDF.oddeven(n)
 
    elif choice == 2:
        n1 = int(input("enter n1: ")) 
        n2 = int(input("enter n2: ")) 
        print("*"*50)
        UDF.maxoftwo(n1,n2)
        
    elif choice == 3:
        n1 = int(input("enter 1: "))
        n2 = int(input("enter n2: "))
        n3 = int(input("enter n3: "))
        print("*"*50)
        UDF.maxofthree(n1,n2,n3)
            
    elif choice == 4:
        n = int(input("enter n: "))
        print("*"*50)
        UDF.prime(n)
        
    elif choice == 5:
        n = int(input("enter n: "))
        print("*"*50)
        UDF.fibonacci(n)     
        
    else:
        print("GOOD BYE")
        break          

 
 