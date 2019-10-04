import cv2
import numpy as np

img1 = cv2.imread('1.jpg')
cv2.imshow('img',img1)
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

cv2.waitKey(0)

