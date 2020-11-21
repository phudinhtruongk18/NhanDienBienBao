import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import pyautogui


def switchAnswer(argument):
    switcher = {
        "đáp án a": [670, 504],
        "đáp án b": [1237, 507],
        "đáp án c": [667, 581],
        "đáp án cuối": [1232, 578],
        "đóng chương trình": [11, 11],
        "kết thúc": [5, 5]
    }
    print("Đã Chọn ",argument.lower())
    return switcher.get(argument.lower(), [69, 69])
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

playsound.playsound('welcome.mp3')
while True:
    playsound.playsound('xacNhan.mp3')
    temp = get_audio()
    temp = format(temp)
    temp = switchAnswer(temp)
    print()
    if temp != [69, 69]:
        if temp == [5, 5]:
            break
        if temp == [11, 11]:
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')
            break
        pyautogui.click(temp)
playsound.playsound('thankfor.m4a')

# speak(temp)
# speak("tôi sẽ bấm chuột giúp bạn?")
