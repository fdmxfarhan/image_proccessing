import cv2

cap = cv2.VideoCapture(0)

while True:
    o, frame = cap.read()
    cv2.imshow('tasvir', frame)
    
cv2.waitKey(0)

             
