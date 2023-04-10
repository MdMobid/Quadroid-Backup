import openai
import speech_recognition as sr
import pyttsx3
import time
from playsound import playsound

 
x=0 #a fleg to check if control is out of assestent
ll=[] #
go=False # to check if weak up call is done
c1=False #to allow first question after weak up call
# Initialize OpenAI API
openai.api_key = "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"
# Initialize the text to speech engine 
engine=pyttsx3.init()



mss=[{'role':'system','content':'your are a smart tech savvy mentor and your name is Dodo ,and are your created by kv number 1 saltlake curious squad'}]

def generate_response(prompt):
    
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

def main():
    global go
    global c1
    global x
    while True:
        tt=time.time()
        if go ==False:
         if x ==0:
             print()
             playsound("sound effect\\mixkit-retro-game-notification-212.wav")
         with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            x=1
        try:
            if go == False:
             
                 
             transcription = recognizer.recognize_google(audio)
        
             if "hey" in transcription.lower() :  
                playsound("sound effect\\the-notification-email-143029.mp3")
                go=True
                c1=True
                tt1=time.time() 
                #time.sleep(2)
                
            while go: 
                playsound("sound effect\\interface-124464.mp3") 
                print("Say Something...")
                speak_text("Say Something")
                c2=int(time.time()-tt1)
                
                if c2>20:
                    go=False
                    x=0  
                filename = "input.wav"
                   
                with sr.Microphone() as source:
                 recognizer = sr.Recognizer()
                 source.pause_threshold = 20
                 audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                 with open(filename, "wb") as f:
                     f.write(audio.get_wav_data())
                audio_file= open("input.wav", "rb")
                transcript = openai.Audio.translate("whisper-1", audio_file)
                text=transcript["text"]
                cc=text.split()
                print("tttex",tt-time.time())

                if text == "Thank you." :
                    print('ttt')
                    continue

                if text:
                    print("Got it..")
                    playsound("sound effect\\mixkit-retro-game-notification-212.wav")
                    tt1=time.time()
                    c1=False
                    print(f"You said: {text}")
                    tt=time.time()

                    # generate the response
                    response = generate_response(text)
                    print(f"Assistant: {response}")
                    print(tt-time.time())


                    # read response using GPT-3
                    speak_text(response)
                    print("Listening...")

        except Exception as e:
                speak_text("Didn't Got That, Please Try Again")
                print("An error occurred: {}".format(e))

if __name__=="__main__":
    main()
