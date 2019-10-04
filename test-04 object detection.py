import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
cnt1=0

while(1):
    isopen, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    low = np.array([0,130,150])
    up = np.array([30,255,255])
    
    mask = cv2.inRange(hsv, low, up)
    res = cv2.bitwise_and(frame,frame, mask= mask)
#    cv2.imshow('img1',mask)
    cv2.imshow('img2',res)
    cv2.imshow('img3',frame)
    
    k = cv2.waitKey(5)
    if k == 27:
        break

cv2.destroyAllWindows()
