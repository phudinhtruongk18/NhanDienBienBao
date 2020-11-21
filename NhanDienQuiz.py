import speech_recognition as sr
import tkinter as jra
import cv2
import playsound
import os
import pyautogui


class Application(jra.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Viet Nam Traffic Signs Detector")
        self.master.minsize(500, 500)

        self.sound = jra.Button(self)
        self.sound["text"] = "Hỗ Trợ Bằng Âm Thanh"
        self.sound["command"] = self.nhanDienGiongNoi
        self.sound.pack()

        self.cam = jra.Button(self)
        self.cam["text"] = "Hỗ Trợ Bằng Hình Ảnh"
        self.cam["command"] = self.chuongTrinhNhanDien
        self.cam.pack()

        self.quit = jra.Button(self, text="QUIT", command=root.destroy)
        self.quit.pack()

        self.pack()
        self.mainloop()

    def chuongTrinhNhanDien(self):
        orb = cv2.ORB_create(nfeatures=1000)
        path = "quiz"
        # path = "bienbao/demo"
        listAnh = []
        listNameAnh = []
        myList = os.listdir(path)

        for name in myList:
            imgNow = cv2.imread(f'{path}/{name}', 0)
            listAnh.append(imgNow)
            listNameAnh.append(os.path.splitext(name)[0])
        print(listNameAnh)

        def timDacDiem(listPic):
            NhanDang = []
            for anh in listPic:
                diemKhac, dinhDanh = orb.detectAndCompute(anh, None)
                NhanDang.append(dinhDanh)
            return NhanDang

        def timID(trucTiep, NhanDang, phucTap):
            diemKhac2, dinhDanh2 = orb.detectAndCompute(trucTiep, None)
            bf = cv2.BFMatcher()
            listGiong = []
            ketLuan = -1
            try:
                for des in NhanDang:
                    matches = bf.knnMatch(des, dinhDanh2, k=2)  # 2 value can compare on
                    good = []
                    for m, n in matches:
                        if m.distance < 0.75 * n.distance:
                            good.append([m])
                    listGiong.append(len(good))
            except:
                pass
            if len(listGiong) != 0:
                if (max(listGiong)) > phucTap:
                    ketLuan = listGiong.index(max(listGiong))
            return ketLuan

        Nhandang = timDacDiem(listAnh)
        print(len(Nhandang))
        quay = cv2.VideoCapture(0)
        while True:
            success, live = quay.read()
            liveMauSac = live.copy()
            live = cv2.cvtColor(live, cv2.COLOR_BGR2GRAY)
            tenCuaAnh = timID(live, Nhandang, 10)
            if id != -1:
                cv2.putText(liveMauSac, listNameAnh[tenCuaAnh], (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (250, 86, 206),
                            3)
            diemKhacBiet, dinhDanhBiet = orb.detectAndCompute(live, None)

            keypoint = cv2.drawKeypoints(live, diemKhacBiet, None)
            cv2.imshow("key point", keypoint)

            cv2.imshow("Phan Mem Ho Tro Quiz", liveMauSac)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    def nhanDienGiongNoi(self):
        def switchAnswer(argument):
            switcher = {
                "đáp án a": [670, 504],
                "đáp án b": [1237, 507],
                "đáp án c": [667, 581],
                "đáp án cuối": [1232, 578],
                "đóng chương trình": [11, 11],
                "kết thúc": [5, 5]
            }
            print("Đã Chọn ", argument.lower())
            return switcher.get(argument.lower(), [69, 69])

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


root = jra.Tk()
app = Application(master=root)
