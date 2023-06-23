#write a python program to check whether an element exists within a tuple.

my_tuple = (10,"my",20,25.5,"name",100)
element = 200

print("Element exists in my_tuple: ",element in my_tuple)
                          #or
if element in my_tuple:
    print("Element:",element,"exists")
else:
    print("Element",element,"does not exist")    
