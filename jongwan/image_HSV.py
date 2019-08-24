#Hue(색상) : 색의 질 0~180, Saturation(채도) : 색의 선명도 0~255, Value(명도) : 색의 밝기 0~255
import cv2
src = cv2.imread("Image/tomato.jpg", cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
#초기 속성은 BGR이므로, cv2.cvtColor()를 이용하여 HSV채널로 변경합니다.
#각각의 속성으로 분할하기 위해서 cv2.split()을 이용하여 채널을 분리합니다.
#Tip : 분리된 채널들은 단일 채널이므로 흑백의 색상으로만 표현

cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''#특정색상출력
import cv2

src = cv2.imread("Image/tomato.jpg", cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

h = cv2.inRange(h, 8, 20)
orange = cv2.bitwise_and(hsv, hsv, mask = h)
orange = cv2.cvtColor(orange, cv2.COLOR_HSV2BGR)

#Hue의 범위를 조정하여 특정 색상만 출력할 수 있습니다.
#cv2.inRange(단일 채널 이미지, 최솟값, 최댓값)을 이용하여 범위를 설정합니다.
#주황색은 약 8~20 범위를 갖습니다.
#이 후, 해당 마스크를 이미지 위에 덧씌워 해당 부분만 출력합니다.
#cv2.bitwise_and(원본, 원본, mask = 단일 채널 이미지)를 이용하여 마스크만 덧씌웁니다.
#이 후, 다시 HSV 속성에서 BGR 속성으로 변경합니다.

cv2.imshow("orange", orange)
cv2.waitKey(0)
cv2.destroyAllWindows()'''