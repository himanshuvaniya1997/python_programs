#write a python fun that takes a list and returns a new list with unique elements of the first list.

def unique_list(l: list):
    newlist = []
    for x in l:
        if x not in newlist:
            newlist.append(x)
    return newlist        
            
my_list = [1,2,2,3,4,5,5,6,1,7,3,8]
Uniquelist = unique_list(my_list)
print(Uniquelist)
