#code for auto create dict for num = square of num / keys = square of keys
'''
n = int(input("enter the num: "))

my_dict = {}

for i in range(1,n+1):
    my_dict[i] = i*i
    
print(my_dict)    
'''
#code for auto create dict for num is divided by 7 and num not divided by 5. upto the range of num.

n = int(input("enter the num: "))

my_dict = {}
for i in range(1,n+1):
    if i%7 == 0 and i%5 != 0: 
        my_dict[i] = i
print(my_dict)        

#code for auto create dict for num is divided by 7 and num not divided by 5.
#using list comprehension.
'''
n1 = range(1,10)

create_dict = {x:x for x in n1 if x%7 == 0 and x%5 != 0}
print(create_dict)
'''                      
                       #or
n1 = int(input("enter the num1: "))

create_dict = {x:x for x in range(1,n+1) if x%7 == 0 and x%5 != 0}
print(create_dict)







        