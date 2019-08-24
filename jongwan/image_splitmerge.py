import cv2

src = cv2.imread("Image/sosage.jpg", cv2.IMREAD_COLOR)

b = src[:,:,0]
g = src[:,:,1]
r = src[:,:,2]
#이미지[높이, 너비, 채널]을 이용하여 특정 영역의 특정 채널만 불러올 수 있습니다.
#:, :, n을 입력할 경우, 이미지 높이와 너비를 그대로 반환하고 n번째 채널만 반환하여 적용합니다.

#b, g, r = cv2.split(src)
#b, g, r = cv2.split(이미지)를 이용하여 채널을 분리
#채널에 순서의 맞게 각 변수에 대입
#분리된 채널들은 단일 채널이므로 흑백의 색상으로만 표현

inversebgr = cv2.merge((r, g, b))
#cv2.merge((채널1, 채널2, 채널3))을 이용하여 나눠진 채널을 다시 병합 가능
#채널을 변형한 뒤에 다시 합치거나 순서를 변경하여 병합 가능
#순서가 변경될 경우, 원본 이미지와 다른 색상으로 표현

cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
cv2.imshow("inverse", inversebgr)
cv2.waitKey(0)
cv2.destroyAllWindows()