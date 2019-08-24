import cv2

src = cv2.imread("Image/pawns.jpg", cv2.IMREAD_COLOR)
dst = src.copy()
#이미지는 numpy 형식과 동일 이미지를 복제할 때, dst=src로 사용할 경우, 원본에도 영향
#그러므로, *.copy()를 이용하여 dst에 이미지를 복제
dst = src[100:600, 200:700]
#dst 이미지에 src[높이(행), 너비(열)]에서 잘라낼 영역을 설정 List형식과 동일
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''import cv2

src = cv2.imread("Image/pawns.jpg", cv2.IMREAD_COLOR)
dst = src.copy() 
roi = src[100:600, 200:700]
#roi를 생성하여 src[높이(행), 너비(열)]에서 잘라낼 영역을 설정. List형식
dst[0:500, 0:500] = roi
#이후, dst[높이(행), 너비(열)] = roi를 이용하여 dst 이미지에 해당 영역을 붙여넣기

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()'''