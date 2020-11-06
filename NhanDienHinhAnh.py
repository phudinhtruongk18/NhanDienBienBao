import cv2
import numpy as np
import os

orb = cv2.ORB_create(nfeatures=1000)

path = "test"
listAnh = []
listNameAnh = []
myList = os.listdir(path)
print(myList)
print("tat ca file la", len(myList))

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
while (True):
    success, live = quay.read()
    liveMauSac = live.copy()
    live = cv2.cvtColor(live, cv2.COLOR_BGR2GRAY)

    tenCuaAnh = timID(live, Nhandang, 15)
    if id != -1:
        cv2.putText(liveMauSac, listNameAnh[tenCuaAnh],(50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

    cv2.imshow("laichym", liveMauSac)
    cv2.waitKey(1)

# imgKpA = cv2.drawKeypoints(imgA, kpA, None)
# imgKpTrain = cv2.drawKeypoints(imgTrain,kpTrain,None)
#
# bf = cv2.BFMatcher() #bruce force
# matches = bf.knnMatch(desA, desTrain, k=2) # 2 value can compare on
#
# good = []
# for m,n in matches:
#     if m.distance < 0.75*n.distance:
#         good.append([m])
# print(len(good))
# imgTemp = cv2.drawMatchesKnn(imgA, kpA, imgTrain, kpTrain, good, None,flags=2)
#
# cv2.imshow("kp1",imgKpA)
# cv2.imshow("kpTrain",imgKpTrain)
# cv2.imshow("cauA", imgA)
# cv2.imshow("Train", imgTrain)
# # cv2.imshow("Train2", imgTrain2)
# cv2.imshow("img Match",imgTemp)
# cv2.waitKey(0)
