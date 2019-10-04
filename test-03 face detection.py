import cv2
import sys

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x+w, y+h), (0, 200, 0), 3)

cv2.imshow('Video', img)
cv2.waitKey(0)

