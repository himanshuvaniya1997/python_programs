#write python program that user to enter only odd numbers, else will raise an exception.

num = int(input("Enter an odd number: "))
try:
    if num%2 == 0:
        raise Exception("Please enter only odd numbers")  
    else:
        print("Entered Num Is Odd: ",num)
except Exception as e:
    print("Exception occur: ",e)
