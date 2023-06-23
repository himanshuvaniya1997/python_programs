#WAP to returns sum of all divisors of a number.

divisors = []
def sum_of_divisors(num):
    for i in range(1,int(num/2)+1):
        if num%i == 0:
           divisors.append(i)  
    return sum(divisors)  
sum = sum_of_divisors(10)
print("Sum Of All Divisors: ",sum)
