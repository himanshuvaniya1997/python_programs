
'''
my_str = input("enter the string: ")
s1 = "not"
s2 = "poor"
count = 0
count1 = 0
j = 0

if "not" and "poor" in my_str:
    x = my_str.index("not")
    y = my_str.index("poor")

    for i in range(0,len(my_str)):
        if count1 != 1:    
            if my_str[i] == s1[j]:
                j = j+1
            elif my_str[i] == s1[0]:
                j = 1
            else:
                j = 0
            if j == len(s1):
                count = count + 1
                j = 0                                      
    print("count for not: ",count)
    if count == 1 and x<y:
        j == 0
        for i in range(0,len(my_str)):
            if my_str[i] == s2[j]:
                j = j+1
            elif my_str[i] == s2[0]:
                j = 1
            else:
                j = 0
            if j == len(s2):
                count1 = count1 + 1
                j = 0               
    print("count1 for poor: ",count1)

    if count == 1 and count1 == 1:
        print(my_str.index("not"))
        snot = my_str[0:my_str.index("not")] 
        print(snot)
        print(my_str.index("poor"))
        spoor = my_str[my_str.index("poor")+4:] 
        print(spoor)

        my_str = snot +"good"+ spoor
        print("Resulting string: ",my_str)
    else:
        print("not doesnt follow poor")    
else:
    print("MISSING SUB STRING")
'''
'''
def long_list(l1: list,l2: list):
    if len(l1) > len(l2):
        return len(l1)
    else:
        return len(l2)

l1 = input("ENTER THE LIST1: ")
l2 = input("ENTER THE LIST2: ")

long_list(l1, l2)
x = long_list(l1, l2)
print("length of longest word: ",x)
'''
'''
import random

data = open("data.txt","w")
for i in range(10):
    num = random.randint(1,100)
    data.write(str(num)+",")
data.close()

data = open("data.txt","r")
even = open("even.txt","w")
odd  = open("odd.txt","w")
prime = open("prime.txt","w")

l = data.read().split(",") [:-1]
print(l)   

for j in l:
    if int(j)%2 == 0:
        even.write(j+",")
    else:
        odd.write(j+",") 
        j = int(j)

for x in l:
    if int(x)%2 != 0:
        x = int(x)
        for y in range(3,int(x/2)+1,2):
            if int(x)%y == 0:
                break
        else:
            x = str(x)
            prime.write(x+",")
    else:
        print("is not prime")
                                    
odd.close() 
even.close()  
data.close() 
prime.close() 

print("data file content: ")
data = open("data.txt","r")
print(data.read())
data.close()

print("even file content: ")
even = open("even.txt","r")
print(even.read())
even.close()

print("odd file content: ")
odd = open("odd.txt","r")
print(odd.read())
odd.close()

print("prime file content: ")
prime = open("prime.txt","r")
print(prime.read())
prime.close()      
'''
'''
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr     #assigned sr = speech_recognition
import pyttsx3

#speech to text conversation 
r = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        print("Speech something: ")
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
            print("you said: {}".format(text))
            print(format(text))
        except:
            print("sorry could not recognize your voice:") 
            text = "sorry could not recognize your voice" 
            audio = pyttsx3.init()
            audio.setProperty('rate', 120)
            audio.setProperty('volume', 50)
            audio.say("sorry could not recognize your voice")
            audio.runAndWait()   
            break 
            
        #text to speech conversation    
        language = "en"
        text = format(text)
        print(text)

        #comaparision between speech and text.
        if  text == "hello":
            audio = pyttsx3.init()
            audio.setProperty('rate', 120)
            audio.setProperty('volume', 50)
            audio.say("welcome to artificial intelligence")
            audio.runAndWait()  
        elif text == "how are you":
            audio = pyttsx3.init()
            audio.setProperty('rate', 120)
            audio.setProperty('volume', 50)
            audio.say("i am fine. and what about you?")
            audio.runAndWait()
        elif text == "who are you":
            audio = pyttsx3.init()
            audio.setProperty('rate', 120)
            audio.setProperty('volume', 50)
            audio.say("i am robot speed 1 terahertz memory 1 certabite.")
            audio.runAndWait()
            playsound(myrobot)    
        else:
            audio = pyttsx3.init()
            audio.setProperty('rate', 120)
            audio.setProperty('volume', 50)
            audio.say("i dont understand what you meant. please speak properly.")
            audio.runAndWait() 
'''
'''
l = [100,500]
print(len(l))
l[1] = 200
print(l)
'''

list_of_dictionaries = [{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
l = list_of_dictionaries

counter = {}
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i].get('item') == l[j].get('item'):
            counter[l[i].get('item')] = l[i].get('amount') + l[j].get('amount')
        else:
            counter[l[i].get('item')] = l[i].get('amount')  
print(counter)   













    








    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    