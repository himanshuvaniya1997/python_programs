#simple addition
'''
a = 10 
b = 20
c = a + b
print("Addition : ",c)
'''
#take input from user without defined data type so o/p is concat.
'''
a = input("enter A: ")
b = input("enter B: ")
c = a + b
print("Addition: ",c)
'''
#take input from user with defined int data type so o/p is addition.
'''
a = int(input("enter A: "))
b = int(input("enter B: "))
c = a + b
print("Addition: ",c)
'''
#find positive or negative number
'''
a = int(input("enter A: "))
if a>0:
    print("a is Positive number")
else:
    print("a is Negative number")
'''
#find the num is even or odd  
'''  
a = int(input("enter A: "))
if a%2 == 0:
    print("a is even number")
else:
    print("a is odd number")
'''
#find max num out of two num.
'''
a = int (input("enter the a: "))
b = int (input("enter the b: "))
if a>b:
    print("a is a maximum num")
else:
    print("b is a maximum num")    
'''
#find max num out of given three numbers.
'''
a = int (input("enter the a: "))
b = int (input("enter the b: "))
c = int (input("enter the c: "))

if a>b:
    if a>c:
        print("a is a max num")
    else:
        print("c is a max num")
elif b>c:
        printf("b is a max num")
else:
    print("c is a max num")        
'''
#find percentage and class of students.
'''
rno = int(input("enter the roll no. : "))
sname =  input("enter the student name: ")
sub1 = int(input("enter the marks of subject 1: "))               
sub2 = int(input("enter the marks of subject 2: "))               
sub3 = int(input("enter the marks of subject 3: "))

total = sub1+sub2+sub3 
perce = total/3

print("rol no. : ",rno)
print("student name : ",sname)
print("total marks : ",total)
print("percentage : ",perce)
              
if perce >= 70:
    print("distiction")
elif perce >= 60:
    print("first class")
elif perce >= 50:
    printf("second class")
elif perce >= 40:
    print("pass class")
else:
    print("FAIL")                          
'''      

