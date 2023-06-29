#without the used of Exception handling.
'''
print("start code")

a = int(input("enter a: "))
b = int(input("enter b: "))
c = a/b
print("division: ",c)

print("end code")
'''
'''
#with using Exception handling.
try:
    print("start code")

    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = a/b
    print("division: ",c)
    
    l = [1,2,3,4,5]
    index = int(input("enter the index: "))
    print(l[index])

except ZeroDivisionError as e:
    print("Exception caught:",e)
except ValueError as e:
    print("Exception caught:",e)    
except IndexError as e:
    print("Exception caught:",e)  
      
print("end code")
'''

#with using base class Exception. all run time Exception = Exception.
try:
    print("start code")

    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = a/b
    print("division: ",c)
    
    l = [1,2,3,4,5]
    index = int(input("enter the index: "))
    print(l[index])

except Exception as e:        #all run time Exception included in Exception.
    print("Exception caught:",e)
finally:
    print("finally block called")    
      
print("end code")















