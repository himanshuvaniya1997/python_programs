#get a single string from two given strings,seperated by space & swap 1st two char of each string. 

s1 = "Himanshu"
s2 = "Vaniya"
s3 = s1 +" "+ s2
print(s3)
for i in range(0,len(s3)):
    if s3[i] == ' ':
        print("if space")
        print("swapping b/w i+1 and i+2")
        temp = s3[i+2]
        s3[i+2] = s3[i+1]
        s3[i+1] = temp
        
    if i == 0:
        print("if 0th index")
        print("swapping b/w i and i+1")
        s3 = list(s3)
        temp = s3[1]
        s3[1] = s3[0]
        s3[0] = temp
print(s3) 

my_str = " "  
for x in s3:
    my_str += ""+ x
print(my_str)    
