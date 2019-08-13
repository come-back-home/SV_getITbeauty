import dlib, cv2, os
from imutils import face_utils
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

path = 'dog_dataset'
detector = dlib.cnn_face_detection_model_v1('dogHeadDetector.dat')
imagePaths = [os.path.join(path,f) for f in os.listdir(path)]  

PIL_img = Image.open('dog_dataset/Dog.1.1.jpg').convert('L') # convert it to grayscale
img_numpy = np.array(PIL_img,'uint8')
dog_image = cv2.imread('dog_dataset/Dog.1.1.jpg',cv2.IMREAD_COLOR)
dets = detector(img_numpy, upsample_num_times=1)
for i, d in enumerate(dets):    
	print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(i, d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom(), d.confidence))

	x1, y1 = d.rect.left(), d.rect.top()
	x2, y2 = d.rect.right(), d.rect.bottom()
	cv2.rectangle(dog_image, pt1=(x1, y1), pt2=(x2, y2), thickness=2, color=(255,0,0), lineType=cv2.LINE_AA)

cv2.imshow('video',dog_image)   
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
for imagePath in imagePaths:
	print(imagePath)
	dog_image = cv2.imread(imagePath)
	dog_image = cv2.cvtColor(dog_image, cv2.COLOR_BGR2RGB)
	cv2.imshow('video',dog_image)
'''