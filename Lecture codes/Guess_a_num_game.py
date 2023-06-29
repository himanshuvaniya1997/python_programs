import random

num = random.randint(1, 10)

while True:
    guess = int(input("Guess a one num between 1 to 10: "))
    if guess == num:
        print("Guess a Correct num")
        break
    elif guess > num:
        print("Correct num is less than the guess num.")    
    elif guess < num:
        print("Correct num is greater than the guess num")     