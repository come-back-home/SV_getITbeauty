import dlib, cv2, os
from imutils import face_utils
import numpy as np
import matplotlib.pyplot as plt

detector = dlib.cnn_face_detection_model_v1('dogHeadDetector.dat')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while True:
	ret, img = cap.read()
	img = cv2.flip(img, 1) # 상하반전
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	dets = detector(img, upsample_num_times=1)

	print(dets)


	for i, d in enumerate(dets):	
	    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(i, d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom(), d.confidence))

	    x1, y1 = d.rect.left(), d.rect.top()
	    x2, y2 = d.rect.right(), d.rect.bottom()

	    cv2.rectangle(img, pt1=(x1, y1), pt2=(x2, y2), thickness=2, color=(255,0,0), lineType=cv2.LINE_AA)

	cv2.imshow('video',img) # video라는 이름으로 출력
	k = cv2.waitKey(30) & 0xff
	if k == 27: # press 'ESC' to quit # ESC를 누르면 종료
		break
cap.release()
cv2.destroyAllWindows()