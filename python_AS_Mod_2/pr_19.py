#write python program to get str made of first 2 & last 2 char from a given str.
#if given str length is <2 return empty string.

def made_str(s):
    str_len = len(my_str)
    if str_len < 2:
        new_str = []
        return new_str
    else: 
        new_str = my_str[:2] + my_str[-2:]
        return new_str 
    
my_str = "himanshu"
return_str = made_str(my_str)    
print(return_str)
