#    01234567890123456    <=positive index 0 to 16.
s = "Tops Technologies" 
#    76543210987654321    <=negative index -17 to -1.

print(s[0:17])
print(s[0:4])
print(s[5:17])
print(s[1:15:2])    #range of index is 1 to 15-1=14
print(s[:14])
print(s[5:])
print(s[::5])

print(s[-15:-2])
print(s[-17:-7:2])
print(s[:-1])
print(s[-14:])
print(s[::-1])


