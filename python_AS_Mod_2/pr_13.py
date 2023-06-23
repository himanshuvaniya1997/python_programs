#count the each word in a given sentence.

sen = input("enter the sentense: ")
count = 0
for i in sen:
    if i.isspace():
        count = count + 1
print("no. of word: ",count+1)        
