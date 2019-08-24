import cv2

src = cv2.imread("Image/fruits.jpg", cv2.IMREAD_COLOR)

height, width, channel = src.shape
#밑줄에서 높이와 너비를 이용해 결과이미지의 크기 설정
dst = cv2.pyrUp(src, dstsize=(width*2, height*2), borderType=cv2.BORDER_DEFAULT);
'''cv2.pyrUp(원본 이미지)로 이미지를 2배로 확대할수 있음
cv2.pyrUp(원본 이미지, 결과 이미지 크기, 픽셀 외삽법)을 의미
결과 이미지 크기는 pyrUp()함수일 경우, 이미지 크기의 2배로 사용
픽셀 외삽법은 이미지를 확대 또는 축소할 경우, 영역 밖의 픽셀은 추정해서 값을 할당
이미지 밖의 픽셀을 외삽하는데 사용되는 테두리 모드. 외삽 방식을 설정'''
dst2 = cv2.pyrDown(src);
'''cv2.pyrDown(원본 이미지)로 이미지를 1/2배로 축소할 수 있음
cv2.pyrUp() 함수와 동일한 매개변수
결과 이미지 크기는 (width/2, height/2)를 사용
'''
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#pyrUp()과 pyrDown() 함수에서 결과 이미지 크기와 픽셀 외삽법은 기본값으로 설정된 인수를 할당해야하므로 생략하여 사용합니다.
#피라미드 함수에서 픽셀 외삽법은 cv2.BORDER_DEFAULT만 사용할 수 있습니다.
#이미지를 1/8배, 1/4배 ,4배, 8배 등의 배율을 사용해야하는 경우, 반복문을 이용하여 적용할 수 있습니다.