import cv2

image = cv2.imread("Image/messi.jpg", cv2.IMREAD_ANYCOLOR) #이미지 불러와 변수에 저장
cv2.imshow("soccer", image) #윈도우창에 이미지 띄움
cv2.waitKey(0)#키입력상태 받아옴 0일경우, 지속적 검사하여 해당구문 넘어가지 않음
cv2.destroyAllWindows() #모든 윈도우창 닫음

'''cv2.IMREAD_UNCHANGED : 원본 사용
cv2.IMREAD_GRAYSCALE : 1 채널, 그레이스케일 적용
cv2.IMREAD_COLOR : 3 채널, BGR 이미지 사용
cv2.IMREAD_ANYDEPTH : 이미지에 따라 정밀도를 16/32비트 또는 8비트로 사용
cv2.IMREAD_ANYCOLOR : 가능한 3 채널, 색상 이미지로 사용
cv2.IMREAD_REDUCED_GRAYSCALE_2 : 1 채널, 1/2 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_GRAYSCALE_4 : 1 채널, 1/4 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_GRAYSCALE_8 : 1 채널, 1/8 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_COLOR_2 : 3 채널, 1/2 크기, BGR 이미지 사용
cv2.IMREAD_REDUCED_COLOR_4 : 3 채널, 1/4 크기, BGR 이미지 사용
cv2.IMREAD_REDUCED_COLOR_8 : 3 채널, 1/8 크기, BGR 이미지 사용'''
height, width, channel = image.shape
print(height, width , channel)