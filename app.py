import tkinter as jra
import cv2
# from PIL import ImageTk
import os

def chuongTrinhNhanDienXe(text):
    orb = cv2.ORB_create(nfeatures=1000)
    path = "bienbao/"+text
    listAnh = []
    listNameAnh = []
    myList = os.listdir(path)

    for name in myList:
        imgNow = cv2.imread(f'{path}/{name}', 0)
        listAnh.append(imgNow)
        listNameAnh.append(os.path.splitext(name)[0])
    print(listNameAnh)

    def timDacDiem(listAnh):
        NhanDang = []
        for anh in listAnh:
            diemKhac, dinhDanh = orb.detectAndCompute(anh, None)
            NhanDang.append(dinhDanh)
        return NhanDang


    def timID(live, NhanDang, phucTap):
        diemKhac2, dinhDanh2 = orb.detectAndCompute(live, None)
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
            cv2.putText(liveMauSac, listNameAnh[tenCuaAnh], (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        cv2.imshow("Phan Mem Nhan Dien Bien Bao Demo", liveMauSac)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


class Application(jra.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Viet Nam Traffic Signs Detector")
        self.master.minsize(500, 150)

        self.khoiDong = jra.Button(self)
        self.khoiDong["text"] = "Biển Báo Chỉ Dẫn"
        self.khoiDong["command"] = self.PressCheck
        self.khoiDong.pack()

        self.khac = jra.Button(self)
        self.khac["text"] = "Biển Báo Lệnh"
        self.khac["command"] = self.PressCheck
        self.khac.pack()

        self.khac1 = jra.Button(self)
        self.khac1["text"] = "Biển Báo Cấm"
        self.khac1["command"] = self.PressCheck
        self.khac1.pack()


        self.khac2 = jra.Button(self)
        self.khac2["text"] = "Biển Báo Nguy Hiểm"
        self.khac2["command"] = self.PressCheck
        self.khac2.pack()

        self.quit = jra.Button(self, text="QUIT", command=root.destroy)
        self.quit.pack()

        self.pack()
        self.mainloop()

    def PressCheck(self, event=None):
        chuongTrinhNhanDienXe('chiDan')


root = jra.Tk()
app = Application(master=root)

