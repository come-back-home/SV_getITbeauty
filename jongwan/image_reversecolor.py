import cv2

src = cv2.imread("Image/whitebutterfly.jpg", cv2.IMREAD_COLOR)

dst = cv2.bitwise_not(src)
#cv2.bitwise_not(원본 이미지)를 이용하여 이미지의 색상을 반전
#비트 연산을 이용하여 색상을 반전시킴 not 뿐만아니라 and, or, xor

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()