#write a program to find the second smallest number in a list.

my_list = [10,40,70,50]
prev_min = min(my_list)

index = my_list.index(min(my_list))
my_list[index] = max(my_list)

small = my_list[0]
for i in my_list:
    if small > i:
        small = i
        
print("Second smallest num: ",small) 
my_list[index] = prev_min
print("Recover prev my list: ",my_list)      
