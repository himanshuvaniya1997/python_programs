#write python program to convert a tuple to a string.

my_tuple = (10,20,"himanshu",50)

'''
tup_to_str = [str(i) for i in my_tuple]  #using list comprehension.
print(tup_to_str)
print(tuple(tup_to_str))
'''
                     #or
conve = []
for i in my_tuple:
    conve.append(str(i))
print(str(conve))    

separetor = ','
new_str = separetor.join(conve)
print("string: ",new_str)
