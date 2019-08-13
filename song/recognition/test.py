import dlib, cv2, os
from imutils import face_utils
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Path for face image database
path = 'dog_dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = dlib.cnn_face_detection_model_v1('dogHeadDetector.dat')

# function to get the images and label data
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')
        print(type(img_numpy))
        id = int(os.path.split(imagePath)[-1].split(".")[1])

        dets = detector(img_numpy, upsample_num_times=1)
        for i, d in enumerate(dets):    
            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(i, d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom(), d.confidence))

            x1, y1 = d.rect.left(), d.rect.top()
            x2, y2 = d.rect.right(), d.rect.bottom()

        #faces = detector.detectMultiScale(img_numpy)
        #for (x,y,w,h) in faces:
            #faceSamples.append(img_numpy[y:y+h,x:x+w])
            #ids.append(id)
    return faceSamples,ids
print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
#recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml
#recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi
# Print the numer of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))