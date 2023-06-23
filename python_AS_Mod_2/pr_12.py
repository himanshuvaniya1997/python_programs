#final code:- count occurences of substring in a string without user input.
            
s1 = "abababbbbabababaaaabbb"                #input("enter the string: ")
s2 = "ab"                         #input("enter the sub-string: ")
print("length of string: ",len(s1))
print("length of sub-string: ",len(s2))

count = 0 
j = 0
for i in range(0,len(s1)-1):
    if s1[i] == s2[j]:
        j = j+1
    elif s1[i] == s2[0]:
        j = 1
    else:
        j = 0
    if j == len(s2):
        count = count + 1
        j = 0                  
                                   
print("total sub-string: ",count)


#final code:- count occurences of substring in a string with user input.
'''            
s1 = input("enter the string: ")
s2 = input("enter the sub-string: ")
print("length of string: ",len(s1))
print("length of sub-string: ",len(s2))

count = 0 
j = 0
for i in range(0,len(s1)-1):
    if s1[i] == s2[j]:
        j = j+1
    elif s1[i] == s2[0]:
        j = 1
    else:
        j = 0
    if j == len(s2):
        count = count + 1
        j = 0                                                    
print("total sub-string: ",count)
'''