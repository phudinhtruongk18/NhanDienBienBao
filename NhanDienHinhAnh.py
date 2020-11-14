import cv2
import os

orb = cv2.ORB_create(nfeatures=1000)
path = "test/chiDan"
#tên đường dẫn đến file cần nhận diện
#t chia thành 3 thư muc cho máy chạy ổn định
#một thư mục chỉ dẩn, 1 thư mục cấm
#và 1 thư mục chỉ dẫn,1 thư mục nguy hiểm
listAnh = []
#chứa các data ảnh để nhận diện
listNameAnh = []
#chứa các tên ảnh trong thư mục
myList = os.listdir(path)
#đọc thư mục

for name in myList:
    imgNow = cv2.imread(f'{path}/{name}', 0)
    listAnh.append(imgNow)
    listNameAnh.append(os.path.splitext(name)[0])
print(listNameAnh)
#đọc các data file ảnh trong thư mục

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
#tìm đặc điểm
print(len(Nhandang))
# in số lương ra console
quay = cv2.VideoCapture(0)
#mở webcam
while True:
#tạo vòng lặp để kiểm tra và nhận diện biển báo
    success, live = quay.read()
    liveMauSac = live.copy()
    live = cv2.cvtColor(live, cv2.COLOR_BGR2GRAY)

    tenCuaAnh = timID(live, Nhandang, 6)
    #nếu đạt những điều kiện t đưa ra thì nó
    # sẽ in text tên ảnh lên màn hình
    if id != -1:
        cv2.putText(liveMauSac, listNameAnh[tenCuaAnh], (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
    cv2.imshow("Phan Mem Nhan Dien Bien Bao", liveMauSac)
    # in lên màn hình
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # bấm q để tắt kết thúc chương trình