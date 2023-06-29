import random

data = open("data.txt","w")
for i in range(10):
    num = random.randint(1,100)
    data.write(str(num)+",")
data.close()

data  = open("data.txt","r") 
even  = open("even.txt","w")
odd   = open("odd.txt","w")
prime = open("prime.txt","w")

l = data.read().split(",") [:-1]
print(l)   

for j in l:                      #loop for separate odd even num 
    if int(j)%2 == 0:
        even.write(j+",")
    else:
        odd.write(j+",") 
        
for x in l:                     #loop for find prime num
    if int(x)%2 != 0:
        x = int(x)
        for y in range(3,int(x/2)+1,2):
            if int(x)%y == 0:
                break
        else:
            x = str(x)
            prime.write(x+",")
    else:
        print("is not prime")        
                
odd.close() 
even.close()  
data.close() 
prime.close() 

print("data file content: ")
data = open("data.txt","r")
print(data.read())
data.close()

print("even file content: ")
even = open("even.txt","r")
print(even.read())
even.close()

print("odd file content: ")
odd = open("odd.txt","r")
print(odd.read())
odd.close()

print("prime file content: ")
prime = open("prime.txt","r")
print(prime.read())
prime.close()      






