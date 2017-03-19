import numpy as np
import cv2

cap = cv2.VideoCapture(0)
 
while(True):
	ret, frame = cap.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)

	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)

	#sobelx = cv2.Sobel(res, cv2.CV_64F, 1, 0, ksize = 5)
	#sobely = cv2.Sobel(res, cv2.CV_64F, 0, 1, ksize = 5)

	abs_grad_x = cv2.convertScaleAbs(sobelx)
	abs_grad_y = cv2.convertScaleAbs(sobely)

	sobel = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

	cv2.imshow('Original in grey', frame)
	cv2.imshow('Laplacian', laplacian)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break

cap.release()
cv2.destroyAllWindows()
