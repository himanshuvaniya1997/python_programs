#check given letter is vowel or not.

letter = input("enter a letter: ")
vowel = "AEIOUaeiou"
#if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
if letter in vowel:     
    print("letter",letter,"is a vowel")
else:    
    print("letter",letter,"is not vowel")
