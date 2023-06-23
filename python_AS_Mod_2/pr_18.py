#write a python fun to reverse a string if its length is a multple of 4.

def revstr(s: str):
    str_len = len(s)
    print(str_len)
    if str_len % 4 == 0:
        s = s[::-1]
        return s
    else:
        print("Length of Given String is not a multiple of 4.")   
    
my_str = input("enter the string: ")
new_str = revstr(my_str)               #call the fun revstr() & store o/p in new_str.
print(new_str)
