#fibonacci series = 0 1 1 2 3 5 8 13 21 34 55 89..... 
#last two num add and its addition is a next num.

a,b = 0,1
n = int(input("enter num: "))

while b<n:
    print(b,end = " ")  #space(" ") for values print in same line. 
    a,b = b,a+b 
print("\n")