import speech_recognition as sr
from gtts import gTTS
import playsound
import os


def switchAnswer(argument):
    switcher = {
        "đáp án a": 1,
        "đáp án b": 2,
        "đáp án c": 3,
        "đáp án cuối": 4
    }
    return switcher.get(argument.lower(), "Null")
    # lower text to compare


# def speak(textToSpeak):
#     print("Bot: {}".format(textToSpeak))
#     tts = gTTS(text=textToSpeak, lang='en')
#     # sử dụng tiếng anh vì không còn hỗ trợ tiếng việt
#     tts.save("xacNhan.mp3")
#     playsound.playsound("xacNhan.mp3")
#     os.remove("xacNhan.mp3")


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi")
            print(text)
            return text
        except:
            print("Phú không thể nghe thấy gì ")
            return 0


temp = get_audio()
temp1 = "ý của bạn là {0}".format(temp)
temp = format(temp)

print(switchAnswer(temp))
# speak(temp)
# speak("tôi sẽ bấm chuột giúp bạn?")
