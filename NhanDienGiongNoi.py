import speech_recognition as sr
from gtts import gTTS
import playsound
import os


def speak(textToSpeak):
    print("Bot: {}".format(textToSpeak))
    tts = gTTS(text=textToSpeak, lang='vi-VN')
    tts.save("xacNhan.mp3")
    playsound.playsound("xacNhan.mp3")
    os.remove("sound.mp3")


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text
        except:
            print("Phú không thể nghe thấy gì ")
            return 0


temp = get_audio()
temp = "ý của bạn là {0}".format(temp)
speak(temp)
speak("bạn chắc chứ?")
speak("tôi sẽ bấm chuột giúp bạn?")
