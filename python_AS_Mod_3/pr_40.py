#write a python fun to check whether a number is in given range.

def is_in_given_range(start,stop,num):
    if num in range(start,stop+1):
        return True 
    else:
        return False    
Ans = is_in_given_range(1, 10, 11)
print(Ans)
