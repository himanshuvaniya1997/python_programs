#make python fun that takes a list of words and returns the len of longest one.

def long_list(l1: list,l2: list):   #user defined function.
    if len(l1) > len(l2):
        return len(l1)
    else:
        return len(l2)

l1 = input("ENTER THE LIST1: ")     #main code.
l2 = input("ENTER THE LIST2: ")

long_list(l1, l2)
x = long_list(l1, l2)
print("length of longest word: ",x)
    