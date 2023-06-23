#WAP to remove an empty tuples(s) from a lists of tupples.

my_list = [(1,2,3),(),(7,8,9),(),(13,14,15),(),(19,20,21)] 
bracket_count = my_list.count(())
for i in range(bracket_count):
    my_list.remove(())   
print(my_list)        
