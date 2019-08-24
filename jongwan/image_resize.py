import cv2

src = cv2.imread("Image/champagne.jpg", cv2.IMREAD_COLOR)

dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
#cv2.resize(원본 이미지, 결과 이미지 크기, 보간법)로 이미지의 크기를 조절
#결과 이미지 크기는 Tuple형을 사용하며, (너비, 높이)
#보간법은 이미지의 크기를 변경하는 경우, 변형된 이미지의 픽셀은 추정
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)
#cv2.resize(원본 이미지, dsize=(0, 0), 가로비, 세로비, 보간법)로 이미지의 크기를 조절
#결과 이미지 크기가 (0, 0)으로 크기를 설정하지 않은 경우, fx와 fy를 이용하여 이미지의 비율을 조절
#fx = 너비 fy = 높이
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''cv2.INTER_NEAREST	이웃 보간법
cv2.INTER_LINEAR	쌍 선형 보간법
cv2.INTER_LINEAR_EXACT	비트 쌍 선형 보간법
cv2.INTER_CUBIC	바이큐빅 보간법
cv2.INTER_AREA	영역 보간법
cv2.INTER_LANCZOS4	Lanczos 보간법

기본적으로 쌍 선형 보간법이 가장 많이 사용됩니다.
이미지를 확대하는 경우, 바이큐빅 보간법이나 쌍 선형 보간법을 가장 많이 사용합니다.
이미지를 축소하는 경우, 영역 보간법을 가장 많이 사용합니다.
영역 보간법에서 이미지를 확대하는 경우, 이웃 보간법과 비슷한 결과를 반환합니다.
'''