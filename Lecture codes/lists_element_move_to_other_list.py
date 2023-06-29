import random

#print(random.randint(1,100))
#print(random.choice([1,10,50,30,66,76]))

l1 = []
l2 = []
for i in range(1,101):
       l1.append(i)
  
for k in range(10):
    r = random.choice(l1)
    
    l2.append(r)
    l1.remove(r)
   
print(l1)
print("l2: ",l2)       


