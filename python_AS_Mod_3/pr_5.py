#write a python fun that takes two lists and return True if they have atleast one common member.     

def common_ele(l1: list,l2: list):
    for i in range(0,len(l1)):
        for j in range(0,len(l2)):
            if l1[i] == l2[j]:
                return True
    else:
        return False        
    
l1 = [1,2,3,4,5]    
l2 = [6,7,1,9,10]

return_value = common_ele(l1, l2)
print("Common Member: ",return_value)
