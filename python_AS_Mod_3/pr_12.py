#write a code for check wethere list contains sublist.

my_list = [10,20,30,[40,50,60]]

for i in my_list:
    print(i) 
    if type(i) == list:
        print("SUB-LIST ARE PRESENT")   
                      #or   used list comprehension.        
#sub_list = [print("SUB-LIST ARE PRESENT")  for i in my_list if type(i) == list]   
