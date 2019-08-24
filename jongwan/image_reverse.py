import cv2

src = cv2.imread("Image/messi.jpg", cv2.IMREAD_COLOR) #원본이미지로 사용할 src선언, 이미지불러옴
dst = cv2.flip(src, 0) #결과 이미지로 사용할 dst선언 대칭함수 적용. 0-상하대칭, 1-좌우대칭
#0보다 낮은값 입력할경우 상하대칭으로 간주, 1보다 높은값 입력할경우 좌우대칭으로 간주

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()