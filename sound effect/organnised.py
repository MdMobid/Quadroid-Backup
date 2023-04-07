import openai
import speech_recognition as sr
import pyttsx3
import time
from playsound import playsound

 
x=0 #a fleg to check if control is out of assestent
ll=[] #
weke=True
go=False # to check if weak up call is done
c1=False #to allow first question after weak up call
# Initialize OpenAI API
openai.api_key = "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"
# Initialize the text to speech engine 
engine=pyttsx3.init()


def role_ass():
 mss=[{'role':'system','content':'your are a smart tech savvy mentor and your name is Dodo'}]
 return mss
def generate_response(prompt):
    
    mss=role_ass()
    mss.append(
        {"role": "user", "content": prompt},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=mss
    )
    reply = chat.choices[0].message.content
    mss.append({"role": "assistant", "content": reply})
    

    return reply

def speak_text(text):
    engine.say(text)
    engine.runAndWait()


def wekeUp():
     global go
     global x
     global c1
     global tt1
     while True:
      try:  
        tt=time.time()
        if go ==False:
         if x ==0:
            playsound("sound effect\\mixkit-retro-game-notification-212.wav")
         with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            x=1
           
        
         if go == False:   
               
             #transcription = recognizer.recognize_google(audio)
             transcription=input("enter the question")
             
             if "hey" in transcription.lower() : 
                print("ok") 
                playsound("sound effect\\the-notification-email-143029.mp3")
                print("step 1 pass")
                go=True
                
                c1=True
                tt1=time.time()
                reply() 
                #time.sleep(2)

        #return (go)    
      except Exception as e:
                print("An error occurred: {}".format(e))     
def sTT():
                global go
                global c1
                global x
                global c2
                global tt
                #print("sptep3 pass temp")
                #go=wekeUp()
                print("sptep3 pass")
                c2=int(time.time()-tt1)
                #print("c2",c2)
                if c2>20:
                    go=False
                    x=0  
                filename = "input.wav"
                    #print("Say your question")
                with sr.Microphone() as source:
                 recognizer = sr.Recognizer()
                 source.pause_threshold = 20
                 audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                 with open(filename, "wb") as f:
                     f.write(audio.get_wav_data())
                #openai.api_key = "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"
                audio_file= open("input.wav", "rb")
                transcript = openai.Audio.translate("whisper-1", audio_file)
                text=transcript["text"]
                #cc=text.split()
                #text=input("question")
                #print("tttex",tt-time.time())

                #if "hey buddy" in text or  cc[0]=="ok" or "dodo"in text.lower():
                #  response = generate_response(text)
                return text
                                  

                 

def reply():
        global go
        global c1
        global x
    
                #if transcription.lower() == "genius":
        try:    
            #wekeUp()
           # sTT()
            while go: 
                print("came back pass")

                playsound("sound effect\\interface-124464.mp3") 
                print("say...")
                text=sTT()
                if text == "Thank you." :
                    print('ttt')
                    continue        

                  # transcript audio to test
                #text = transcribe_audio_to_test(filename)
                if text:
                #if "hey buddy" in text or  cc[0]=="ok" or ("dodo"in text.lower() )or( c1):    
                    print("got it.................")
                    playsound("sound effect\\mixkit-retro-game-notification-212.wav")
                    tt1=time.time()
                    c1=False
                    print(f"You said: {text}")
                    tt=time.time()

                    # generate the response
                    response = generate_response(text)
                    print(f"Chat GPT-3 says: {response}")
                    print(tt-time.time())


                    # read response using GPT-3
                    speak_text(response)
                    print("lissing .....")
        except Exception as e:
                print("An error occurred: {}".format(e))

if __name__=="__main__":
   # main()
   wekeUp()