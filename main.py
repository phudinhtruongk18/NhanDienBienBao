import cv2
import numpy as np

imgA = cv2.imread("quiz/quizA.png",0)

# imgTrain = cv2.imread("quiz/test/anh1.jpg",0) # add 0 to grayscale
imgTrain = cv2.imread("quiz/test/anh3.jpg",0)

orb = cv2.ORB_create(nfeatures=1000)

kpA, desA = orb.detectAndCompute(imgA, None)
kpTrain, desTrain = orb.detectAndCompute(imgTrain, None)
# keyPoint, descriptors
imgKpA = cv2.drawKeypoints(imgA, kpA, None)
imgKpTrain = cv2.drawKeypoints(imgTrain,kpTrain,None)

bf = cv2.BFMatcher() #bruce force
matches = bf.knnMatch(desA, desTrain, k=2) # 2 value can compare on

good = []

for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
print(len(good))
imgTemp = cv2.drawMatchesKnn(imgA, kpA, imgTrain, kpTrain, good, None,flags=2)

cv2.imshow("kp1",imgKpA)
cv2.imshow("kpTrain",imgKpTrain)
cv2.imshow("cauA", imgA)
cv2.imshow("Train", imgTrain)
# cv2.imshow("Train2", imgTrain2)
cv2.imshow("img Match",imgTemp)
cv2.waitKey(0)
