#sum of three given num. and if two num are equal sum = 0.

a = int(input("enter the a: "))
b = int(input("enter the b: "))
c = int(input("enter the c: "))
if a==b or b==c or a==c: 
    s = 0
    print("sum is: ",s)
else:    
    s = a + b + c
    print("sum is: ",s)
