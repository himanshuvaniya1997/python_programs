from gtts import gTTS
from playsound import playsound
import speech_recognition as sr     #assigned sr = speech_recognition

#speech to text conversation 
r = sr.Recognizer()
with sr.Microphone() as source:
    
    while True:
        print("Speech something: ")
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
            print("you said: {}".format(text))
        except:
            print("sorry could not recognize your voice:") 
            text = "sorry could not recognize your voice" 
            language = "en"
            speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
            speech.save("robotn.mp3")
            myrobot = "robotn.mp3"
            playsound(myrobot)
            break
            
        #text to speech conversation    
        language = "en"
        text = format(text)

        #comaparision between speech and text.
        if  text == "hello":
            language = "en"
            text = "hello sir. how are you doing today?"
            speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
            speech.save("robot.mp3")
            myrobot = "robot.mp3"
            playsound(myrobot)
        elif text == "how are you":
            language = "en"
            text = "i am fine. and you?"
            speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
            speech.save("robot1.mp3")
            myrobot = "robot1.mp3"
            playsound(myrobot)
        elif text == "who are you":
            language = "en"
            text = "i am robot. speed 1 terahertz memory 1 certabite."
            speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
            speech.save("robot2.mp3")
            myrobot = "robot2.mp3"
            playsound(myrobot)  
        elif text == "where are you from":
            language = "en"
            text = "i am from virtual world. inside this computer"
            speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
            speech.save("robot3.mp3")
            myrobot = "robot3.mp3"
            playsound(myrobot)              
        else:
            language = "en"
            text = "ask me some questions. i will try to answer you"
            speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
            speech.save("robote.mp3")
            myrobot = "robote.mp3"
            playsound(myrobot)     
    




    