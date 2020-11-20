import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import pyautogui

def switchAnswer(argument):
    switcher = {
        "đáp án a": [670,504],
        "đáp án b": [1237, 507],
        "đáp án c": [667,581],
        "đáp án cuối": [1232, 578],
        "kết thúc": [5,5]
    }
    return switcher.get(argument.lower(), [69,69])
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

while True:
    temp = get_audio()
    temp1 = "ý của bạn là {0}".format(temp)
    temp = format(temp)
    print(switchAnswer(temp))
    if switchAnswer(temp) != [69, 69]:
        if switchAnswer(temp) == [5, 5]:
            break
        pyautogui.click(switchAnswer(temp))



# speak(temp)
# speak("tôi sẽ bấm chuột giúp bạn?")
