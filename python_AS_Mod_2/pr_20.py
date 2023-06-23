#write a python function to insert a string in the middle of a string.

def insert_str(s1: str,s2: str):   #user defined function.
    s1_len = len(s1)
    s2_len = len(s2)
    middle = int(s1_len/2)

    new_str = s1[:middle]+" "+ s2 + s1[middle:]
    return new_str

s1 = "my name vaniya"         #main  code.
s2 = "Himanshu"
new_str = insert_str(s1, s2)   #call the fun.
print(new_str)
