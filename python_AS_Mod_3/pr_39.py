#Write a python function to calculate the factorial of a number(a non negative integer).

def cal_fact_num(n):
    fact = 1
    while n>0:
        fact = fact * n
        n = n-1
    return fact
    
ans = cal_fact_num(5)
print(ans)
