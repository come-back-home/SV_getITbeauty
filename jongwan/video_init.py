import cv2

capture = cv2.VideoCapture("Image/abc.mp4") #동영상 파일에서 프레임 받아옴

while True:
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):#capture.get(속성)을 이용해 capture의 속성반환
        capture.open("Image/abc.mp4")#CAR_PROP_POS_FAMES 는 현재 프레임 개수 CAR_PROP_FRAME_COUNT는 총 프레임 개수
        #같을경우, 마지막프레임이므로 다시 동영상파일 불러옴

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    if cv2.waitKey(33) > 0: break #waitkey 이용해 33ms마다 프레임 재생 , 어떤키라도 누를경우 break하여 while문 빠져나옴

capture.release()
cv2.destroyAllWindows()