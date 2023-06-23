#WAP to find the first appearance of the substring 'not' and 'poor' from a given string,
#if 'not' follows the 'poor',replace the whole 'not'...'poor' substring with 'good'.and
#return the resulting substring.

my_str = input("enter the string: ")
s1 = "not"
s2 = "poor"
count = 0
count1 = 0
j = 0

if "not" and "poor" in my_str:
    x = my_str.index("not")
    y = my_str.index("poor")

    for i in range(0,len(my_str)):
        if count1 != 1:    
            if my_str[i] == s1[j]:
                j = j+1
            elif my_str[i] == s1[0]:
                j = 1
            else:
                j = 0
            if j == len(s1):
                count = count + 1
                j = 0                                      
    print("count for not: ",count)
    if count == 1 and x<y:
        j == 0
        for i in range(0,len(my_str)):
            if my_str[i] == s2[j]:
                j = j+1
            elif my_str[i] == s2[0]:
                j = 1
            else:
                j = 0
            if j == len(s2):
                count1 = count1 + 1
                j = 0               
    print("count1 for poor: ",count1)

    if count == 1 and count1 == 1:
        print(my_str.index("not"))
        snot = my_str[0:my_str.index("not")] 
        print(snot)
        print(my_str.index("poor"))
        spoor = my_str[my_str.index("poor")+4:] 
        print(spoor)

        my_str = snot +"good"+ spoor
        print("Resulting string: ",my_str)
    else:
        print("not doesnt follow poor")    
else:
    print("MISSING SUB STRING")
