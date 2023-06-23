#write a python script to concatenate following dictionaries to create a new one.

d1 = {'a':10,'b':20,'c':30}
d2 = {'d':40,'e':50,'f':60}

d1.update(d2)
concate_dict = d1
print(concate_dict)
                   #or
                
new_dict = {**d1,**d2}                
print(new_dict)        
