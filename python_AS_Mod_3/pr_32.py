#write a python program to map two lists in to dictionary.

l1 = [1,2,3,4,5,6,7,8]
l2 = [10,20,30,40,50,60,70,80]
my_dict = {}
index = 0
for i in l1:
    my_dict[i] = l2[index]
    index = index + 1
print(my_dict)
                  #or
                  
keys = ['name','age','city']
value = ['Himanshu',25,'Ahmedabad'] 

new_dict = dict(zip(keys,value))    
print(new_dict)             
