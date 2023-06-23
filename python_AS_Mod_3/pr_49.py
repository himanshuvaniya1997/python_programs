#WAP to find the maximum and minimum numbers from the specified decimal numbers.

def max(list):
    m = list[0]
    for i in range(len(list)):
        if list[i] > m:
            m = list[i] 
    return m        
def min(list):
    m = list[0]
    for i in range(len(list)):
        if list[i] < m:
            m = list[i] 
    return m   
        
my_list = [2.5,50.55,1.2,10.1,80.23,60.90]
maximum_num = max(my_list)
print("Max num: ",maximum_num)
minimum_num = min(my_list)
print("Min num: ",minimum_num)


