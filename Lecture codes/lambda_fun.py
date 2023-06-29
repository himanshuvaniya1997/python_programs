#1.
str1 = "himanshu vaniya"
rev_upper = lambda str1: str1.upper() [::-1]
print(rev_upper(str1))

#2.
cube = lambda y: y*y*y
print(cube(5))

#3.
sum1 = lambda a,b: a+b
print(sum1(10,20))

#4.
Isbiggest = lambda x,y: x>y 
print(Isbiggest(10,20))

#5.
Issmallest = lambda x,y: x<y 
print(Issmallest(10,20))

#6.
Iseven = lambda x: x%2 == 0 
print(Iseven(10))

#7.
Isodd = lambda x: x%2 != 0 
ans = Isodd(10)
print(int(ans))

#8.
s1 = "himanshu"
s2 = "vaniya"

first_Islong = lambda s1,s2: len(s1) > len(s2) 
print("first string is longest?: ",first_Islong(s1,s2))

#9.
find_pecentage = lambda o,t: o/t*100
print(find_pecentage(346,600))

#10.
string = "himanshu vaniya"
l = len(string)
mid = int(l/2)
print(mid)

first_half = lambda x: (string[0:mid])  
print(first_half(string))
second_half = lambda x: (string[mid:l])  
print(second_half(string))
 
'''                                #or
first_half = lambda x: (string[0:len(string)//2]) #here // is used for integer division.
print(first_half(string))                                
second_half = lambda x: (string[len(string)//2:len(string)])  #here // is used for integer division.
print(second_half(string))
'''

#11.
s111 = "Himanshu"
s222 = "Vaniya"

conca_str = lambda s1,s2: s111 +" "+ s222 
print(conca_str(s111,s222))

#12.
letter = input("enter the one alphabet: ")
vowel = "AEIOUaeiou"
Isvowel = lambda l: letter in vowel
print(Isvowel(letter))

    










