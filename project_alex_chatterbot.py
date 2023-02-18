import speech_recognition 
import pyttsx3
from datetime import date
import time
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def listening():
    print("Alex listening...")	
    robot_ear = speech_recognition.Recognizer() # Tạo ra robot_ear có thể nghe được
    with speech_recognition.Microphone() as mic: # Nghe được với việc sử dụng mic
        audio = robot_ear.listen(mic, phrase_time_limit=5) # audio = robot_ear nghe được bằng mic, với giới hạn thời gian là 5s
    try:
        audio_text = robot_ear.recognize_google(audio) # Nhận dạng âm thanh nghe được ở trên .recognize_google() với ngôn ngữ là tiếng Việt
    except:
        audio_text = ""
    return audio_text



def speaking(text):

    engine = pyttsx3.init() #Khởi tạo biến engine có thể nói được

    voices = engine.getProperty('voices') #Khởi tạo voices có thể chỉnh sửa 
    engine.setProperty("voice", voices[1].id) #Chỉnh sửa  thành giọng nữ [1]

    engine.say(text) #Chuyền biết văn bản text vào hàm say()
    engine.runAndWait() #Chạy biến engine khi đã được chỉnh sửa và truyền văn bản cần đọc


def chatter_bot(info):

    chatbot = ChatBot("Chatpot")

    trainer = ListTrainer(chatbot)
    trainer.train([
        "Hi",
        "Welcome, friend 🤗",
    ])
    trainer.train([
        "Are you a plant?",
        "No, I'm the pot below the plant!",
    ])
    trainer.train([
        "How are you ?",
        "I am fine, thank you",
    ])
    speaking(f"🪴 {chatbot.get_response(info)}")
    return


def get_time(text):
    now = ""
    if "today" in text:
        today = date.today()
        day = today.strftime("%B %d, %Y")
        now = "Today is %s" %day
    if "time" in text:
        now = time.strftime("It is %H:%M", time.localtime())
    speaking(now)
    return


def hello():

    day_time = int(time.strftime('%H'))
    if day_time < 12:
        speaking("Good morning. Have a good day")
    elif 12 <= day_time < 18:
        speaking("Good afternoon. What have you planned for this afternoon")
    else:
        speaking("Good evening. Have you had dinner yet")
    return

def main():

    hello()

    while True:
        info = listening()

        exit_conditions = ("goodbye", "bye", "quit", "exit")
        
        if info in exit_conditions:
            print("Bye Bye 👋👋")
            speaking("Goodbye, see you again !!!")
            break
        elif ("today" or "time") in info:
            get_time(info)
        else:
            chatter_bot(info)

if __name__ == "__main__":
    main()
