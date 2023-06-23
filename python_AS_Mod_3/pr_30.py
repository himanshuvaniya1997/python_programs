#write a python program to check multiple keys exists in a dictionary.

my_dict = {'a':10,'b':20,'c':30,'d':40}
multiple_keys = ['a','c']
for key in my_dict:
    if key in multiple_keys:
        print(key,"Exists in my_dictionary")
    else:
        print(key,"Does not exists in my_dictionary")
