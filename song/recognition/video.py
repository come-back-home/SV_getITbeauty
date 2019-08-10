import dlib, cv2, sys
from imutils import face_utils
import numpy as np

SCALE_FACTOR = 0.2

detector = dlib.cnn_face_detection_model_v1('dogHeadDetector.dat')


video_path = "./video/22.mp4"
cap = cv2.VideoCapture(video_path)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#out = cv2.VideoWriter('./dataset/%s_output.mp4' % (video_path.split('/')[-1].split('.')[0]), fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

face_id = 1
count = 0

while cap.isOpened():
  ret, img = cap.read()

  if not ret:
    break

  img_result = img.copy()

  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  img_dataset = img.copy()
  img = cv2.resize(img, dsize=None, fx=SCALE_FACTOR, fy=SCALE_FACTOR)

  dets = detector(img, upsample_num_times=1)

  for i, d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(i, d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom(), d.confidence))

    x1, y1 = int(d.rect.left() / SCALE_FACTOR), int(d.rect.top() / SCALE_FACTOR)
    x2, y2 = int(d.rect.right() / SCALE_FACTOR), int(d.rect.bottom() / SCALE_FACTOR)

    cv2.rectangle(img_result, (x1, y1), (x2, y2), thickness=2, color=(255,0,0), lineType=cv2.LINE_AA)

    
    count+=1
    cv2.imwrite("dog_dataset/Dog."+str(face_id)+'.'+str(count)+".jpg",img_dataset[y1:y2,x1:x2])

    '''
    #눈코입 점찍고 숫자 적는부분
    shape = predictor(img, d.rect)
    shape = face_utils.shape_to_np(shape)
    
    for i, p in enumerate(shape):
      cv2.circle(img_result, center=tuple((p / SCALE_FACTOR).astype(int)), radius=5, color=(0,0,255), thickness=-1, lineType=cv2.LINE_AA)
      cv2.putText(img_result, str(i), tuple((p / SCALE_FACTOR).astype(int)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
    '''

  #out.write(img_result)
  cv2.imshow('result', img_result)

  k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
  if k == 27:
      break
cap.release()
#out.release()
