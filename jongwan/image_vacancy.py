import cv2
import numpy as np
src = cv2.imread("Image/tomato.jpg", cv2.IMREAD_COLOR)
b = src[:,:,0]
g = src[:,:,1]
r = src[:,:,2]

height, width, channel = src.shape
zero = np.zeros((height, width, 1), dtype = np.uint8)
bgz = cv2.merge((b, g, zero))

cv2.imshow("vacancy", bgz)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''검은색 빈 공간 이미지가 필요할 때는 np.zeros((높이, 너비, 채널), dtype=정밀도)을 이용하여 빈 이미지를 생성할 수 있다.

Blue, Green, Zero이미지를 병합할 경우, Red 채널 영역이 모두 흑백이미지로 변경

Tip : import numpy as np가 포함된 상태여야 함'''
