#python code for count the num of strings where the string length is 2 or more and 
#the first & last char are same from given list of strings.

def countstr(lst: list):
    count = 0
    for s in lst:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count         
    
l = ['himansh','vaniya','tielist','hutch']
count = countstr(l)
print(count)
