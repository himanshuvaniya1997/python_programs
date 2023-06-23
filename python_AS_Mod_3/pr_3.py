#write a python program to remove duplicates from list.

def remove_dup(d: list):
    new_list = []
    
    for data in d:
        if data not in new_list:
            new_list.append(data)
            
    return new_list

my_list = [1,2,3,5,2,6,7,3]
print("my list:       ",my_list)
no_dupl_list = remove_dup(my_list)
print("No dupli list: ",no_dupl_list)
