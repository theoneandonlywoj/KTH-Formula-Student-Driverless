import cv2
import numpy as np
import time

img = cv2.imread('formula-student-about.jpg', 1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([20, 100, 100])
upper = np.array([30, 255, 255])

mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(img, img, mask= mask)


cv2.imshow('image', img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)


k = cv2.waitKey(0)
#time.sleep(30)


cv2.destroyAllWindows()
cap.release()