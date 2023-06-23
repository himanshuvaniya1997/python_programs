#count the no. of characters in a string.

s = input("Enter the string: ")

ch = 0
nm = 0
spc = 0
up = 0
lw = 0
space = 0

for i in s:
    if i.isalpha():
        ch = ch+1
    elif i.isnumeric():
        nm = nm+1
    elif i.isspace():
        space = space+1
    elif not i.isalnum():   #or else:
        spc = spc+1    
    if i.isupper():
        up = up+1
    if i.islower():
        lw = lw+1   
 
print("total alphabet: ",ch)
print("total numeric: ",nm)
print("total special char: ",spc)
print("total upper char: ",up)
print("total lower char: ",lw)
print("total space: ",space)
