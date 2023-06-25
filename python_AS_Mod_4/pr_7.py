#write a python program to find the longest word from text and longest word from file.

def find_longest_word(text):
    words = text.split()
    print(words)
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word        

text = "this is a python code for find the longest word from text comparision"
longest_word = find_longest_word(text)
print("Longest Word Is: ",longest_word)
print("\n")

                        #OR
                                               
def find_longest_word_from_file(textfile):
    words = textfile.readlines()
    words = str(words).split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word       

myfile = open("textfile.txt","r")
longest_word = find_longest_word_from_file(myfile)
print("Longest Word From File Is: ",longest_word)
myfile.close()
