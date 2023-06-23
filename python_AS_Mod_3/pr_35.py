#WAP to create and display all combinations of letters.selecting each letter from a different key in a dictionary.
#sample data: {'1':['a','b'], '2':['c','d']}
#Expected output: ac ad bc bd

my_dict = {'1':['a','b'], '2':['c','d']}
print(my_dict)
new_list = []

a1 = my_dict['1']
a2 = my_dict['2']

for x in range(2):
    for y in range(2):
       new_list.append(a1[x])
       new_list.append(a2[y])
       new_list.append(" ")
print("Expected Output in list: ",new_list)
my_str = ''.join(new_list)
print("Expected Output in string: ",my_str)
