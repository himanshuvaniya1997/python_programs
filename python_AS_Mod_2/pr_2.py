#find factorial num of given num.   
#factorial of 5  = 5 x 4 x 3 x 2 x 1 =120.   

num = int(input("enter the num: "))
fact = 1
while num>1:
    fact = fact * num
    num = num-1
print("factorial num: ",fact)    
