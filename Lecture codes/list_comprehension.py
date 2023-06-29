'''
#1.
my_list = [i for i in range(1,11)]                   #here variable = i
print(my_list)

#2.
my_list1 = [i for i in range(1,11) if i%2 == 0]       #here variable = i
print(my_list1)

#3.
my_list2 = [[j for j in range(3)] for i in range(3)]  #here variable = [j for j in range(3)]
print(my_list2)

#4.
my_list3 = [i*10 for i in range(1,6)]  #here variable = i*10
print(my_list3)

#5.
my_list4 = [i*i*i for i in range(1,11)]
print(my_list4)

#6.
my_list5 = [1,2,1,1,2,3,4,4,5,5]
unique_num = [list (set(my_list5))]
print(unique_num)

#7. create list in sub-list.
name = ['raj','milan','prince']
age = [20,18,25]
people = [[name,age] for name,age in zip(name,age)]
print(people)

#8.
n = int(input("enter the num: "))
my_list6 = [i for i in range(0,n+1) if i%7 == 0 and i%5 != 0]
print(my_list6)

#9.
ite_str = [letter for letter in 'himanshu']
print(ite_str)

#10.
num_list = [x for x in range(101) if x%2 == 0 if x%5 == 0]
print(num_list)


11.
Odd_even = ["Even" if i%2 == 0 else "odd" for i in range(1,11)]
print(Odd_even)

#12. prime number or not using list comprehension.
n11 = int(input("Enter One Num: "))
if n11%2 != 0:
    prime = ["PRIME" if n11%i != 0   else "not prime" for i in range(3,int(n11/2)+1,2)]
    if "not prime" in prime:
        print(n11,"IS NOT PRIME")
    else:
        print(n11,"IS PRIME NUM")    
else:
    print(n11,"IS NOT PRIME NUM")

#13.
matrix = [[1,2],[3,4],[5,6],[7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)

#14.
numm = int(input("enter the numm: "))
a = [1,2,25,3,4,5,7,34,23,12,6,20]
greater_list = [x for x in a if x > numm]
print(greater_list)

#15.
value = [[1,2,3],[10,50,70],[98,56.75]]
val_max = [max(x) for x in value]
print(val_max)

#16.
let_list = ['himanshu','nesting','asking','simply','making','types']
ends_with = [i for i in let_list if i.endswith('ing')]
print(ends_with)

#17.
listval = [[1,2,3],[4,5,6],[7,8,9]]
newlist_val = [x for y in listval for x in y]
print(newlist_val)

#18.
list_my = ['SRH','rr','GT','LSG','csk','mi','RCB']
Isupper_list = [x for x in list_my if x.isupper()]
print(Isupper_list)
'''
#19.
nyl = ["my","new file","hello","exitement","member"]
len_str = [len(i) for i in nyl ]
print(len_str)

#20.
file_eleme = [1,45,23,46,22,88,10,69,36,100,150]
odd  = open("odd.txt","w")
even = open("even.txt","w")
write_file = [even.write(str(i)+",") if i%2 == 0 else odd.write(str(i)+",") for i in file_eleme]
odd.close()
even.close()

odd  = open("odd.txt","r")
print("odd file content: ",odd.read())
odd.close()
even  = open("even.txt","r")
print("even file content: ",even.read())
even.close()





