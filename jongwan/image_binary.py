import cv2

src = cv2.imread("Image/geese.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
#이진화를 적용하기 위해서 그레이스케일로 변환
#ret, dst를 이용하여 이진화 결과를 저장 ret에는 임계값이 저장
#cv2.threshold(그레스케일 이미지, 임계값, 최댓값, 임계값 종류)를 이용하여 이진화 이미지로 변경
#임계값은 이미지의 흑백을 나눌 기준값을 의미 100으로 설정할 경우, 100보다 이하면 0으로, 100보다 이상이면 최댓값으로 변경
#임계값 종류를 이용하여 이진화할 방법 설정
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()