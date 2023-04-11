import openai
import speech_recognition as sr
import pyttsx3
import time
from playsound import playsound
import webbrowser
from AppOpener import open, close
 
x=0 #a fleg to check if control is out of assestent
ll=[] #
go=False # to check if weak up call is done
c1=False #to allow first question after weak up call
sleep=False
# Initialize OpenAI API
#openai.api_key = "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"
# Initialize the text to speech engine 
engine=pyttsx3.init()


mss=[{'role':'system','content':'you are a smart ai assistant and your name is Quadroid ,and you are created by KV Number 1 Saltlake Curious Squad, and you are to help humans day to day life'}]

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


def open(query):
  print()

  import webbrowser
  from AppOpener import open, close

  while True:
    #query=input("What to open? ")
    query=query
    
    if "in web" in query:
      x=x.replace(" in web","").strip()
      print("OPENING",x)
      webbrowser.open(x)

    elif "open" or "close" in query:

      if "close " in query:
        app_name = query.replace("close ","").strip()
        close(app_name, match_closest=True, output=False) # App will be close be it matches little bit too (Without printing context (like CLOSING <app_name>))
  
      elif "open " in query:
        app_name = query.replace("open ","")
        open(app_name, match_closest=True) # App will be open be it matches little bit too


def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    global go
    global c1
    global x
    global sleep
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
       # try:
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
                
                x=0  
                filename = "input.wav"
                   
                with sr.Microphone() as source:
                 recognizer = sr.Recognizer()
                 source.pause_threshold = 60
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

                if "tell me some" and "news" in text.lower():
                    topic_word = text.split(" ")[3]
                    import requests
                    def get_news(topic):
                          # Make a request to the news API and retrieve articles related to the topic
                          url = f'https://newsapi.org/v2/everything?q={topic}&apiKey=c85f7fc043d3408980c30baa7aeadc25'
                          response = requests.get(url)
                          articles = response.json()['articles']
                          return articles
                    
                    def extract_information(article):
                          # Extract information from the article
                          title = article['title']
                          if 'description' in article:
                               description = article['description']
                          else:
                               description = 'No description available.'
                          return title, description
                    
                    def present_news(articles):
                          # Create a string to store the news articles
                          news_str = ''
                          counter = 1
                          for article in articles:
                              title, description = extract_information(article)
                              news_str += f'{counter}. {title}\n'
                              news_str += f'{description}\n\n'
                              counter += 1
                              if counter == 4:
                                  break
                          return news_str

                    topic = topic_word
                    articles = get_news(topic)
                    news_str = present_news(articles)
                    print(news_str)
                    speak_text(news_str)
                    continue

                if "sleep" in text.lower():
                    go=False
                    sleep=True
                    print("Going to Sleep..")
                    speak_text("OK, Going to sleep, Call me When You Need Me")
                    continue


                if "open" or "close" in text.lower():
                        topic_word = text.split(" ")[3]
                        open( topic_word)
                else:
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

    #    except Exception as e:
    #            if not sleep:
    #                speak_text("Didn't Got That, Please Try Again")
    #                print("An error occurred: {}".format(e))

if __name__=="__main__":
    main()
