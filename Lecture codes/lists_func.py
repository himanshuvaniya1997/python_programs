l = [1,2,1.1,2.2,10,"Tops",True,"python",1,2]

print("length of list l: ",len(l)) 
print(l)     #print object of lists.


for i in l:   
    print(i)   #print individual elements of lists.

#library fun for lists.
    
print(10 in l)  #element 10 is in list l. so print True. 
print(200 in l) #element 200 is not present in list l. so print False.

l.append(100)   #append is used for add new element at the end of the list.
print(l)

'''
l.clear()       #clear is used for full empty the list. 
print(l)
'''
l1 = l.copy()  #copy the elements of list(l) to the list(l1). both list are independent of each other.
print(l1)      #there l and l1 contains two different memory location.
l1.append(200)
print("l: ",l)
print("appended 200 in list l1: ",l1)

l2=l           #copy the elements of list(l) to the list(l2). both list are dependent of each other.
print("l2: ",l2) #there l and l2 contains same memory location with different name l and l2.
l2.append(300)
print("l: ",l)
print("appended 300 in list l2: ",l2)

print(l.count(1))  #count the no. of entered value will occur in list l.

l3 = [1000,2000,3000]
l.extend(l3)        #list(l3) extended at the end of list(l). or merge list l and l3.
print("extended list l: ",l)

print(l.index(10))  #print the index of entered value.

print(l.pop())      #delete or remove the last element of given list.
print("pop last element of l: ",l)

print(l.pop(5))      #delete or remove the element of given index from the given list.
print("pop element at index 5 from l: ",l)

l.remove(10)        #delete or remove the given value from the list.its only remove once.
print("remove 10 l: ",l)

l.reverse()         #reverse the given list.
print("reverse order of l: ",l)





   
