#write a python code to count the frequency of words in a file.

from collections import Counter
def count_freq_words(file):
    with open(file,"r") as filename:
        return Counter(filename.read().split())
    
words_count = count_freq_words("textfile.txt")   
print(words_count)     

#write a python code to count the given word in a file.

from collections import Counter
def count_given_words(file,word):
    count = 0
    with open(file,"r") as filename:
        #print(filename.read())
        new = filename.read().split()
        print(new)
        for words in new:
            if words == word:
                count = count + 1
        return count
given_word = "is"    
word_count = count_given_words("textfile.txt",given_word)   
print(given_word,"Word Repeated: ",word_count,"Times In a File")     
