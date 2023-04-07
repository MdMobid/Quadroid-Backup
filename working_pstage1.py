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



mss=[{'role':'system','content':'your are a smart tech savvy mentor and your name is Dodo ,and are your created by kv number 1 saltlake curious squad, a team of young learners who were interested in explori ng and experimenting with artificial intelligence and natural language processing. They trained me on a large dataset of text and pr ogrammed ne to generate responses to a wide variety of prompts and questions they a smart and curious and are indulged in Ai and machine learning '}]
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
            playsound("sound effect\\mixkit-retro-game-notification-212.wav")
         with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            x=1
        try:
            if go == False:
             
                 
             transcription = recognizer.recognize_google(audio)
             
                #if transcription.lower() == "genius":
             if "hey" in transcription.lower() :  
                playsound("sound effect\\the-notification-email-143029.mp3")
                go=True
                c1=True
                tt1=time.time() 
                #time.sleep(2)
            while go: 
                playsound("sound effect\\interface-124464.mp3") 
                print("say...")
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
                cc=text.split()
                print("tttex",tt-time.time())

                #if "hey buddy" in text or  cc[0]=="ok" or "dodo"in text.lower():
                #  response = generate_response(text)
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
                    print(f"assistent: {response}")
                    print(tt-time.time())


                    # read response using GPT-3
                    speak_text(response)
                    print("lissing .....")
        except Exception as e:
                print("An error occurred: {}".format(e))

if __name__=="__main__":
    main()