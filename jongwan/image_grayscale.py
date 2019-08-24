import cv2

src = cv2.imread("Image/crow.jpg", cv2.IMREAD_COLOR)
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
#cv2.cvtcolor(원본 이미지, 색상 변환 코드)를 이용하여 이미지의 색상 공간을 변경
#색상 변환 코드는 원본 이미지 색상 공간2결과 이미지 색상 공간을 의미합니다.
#원본 이미지 색상 공간은 원본 이미지와 일치해야함
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''CV_8U 이미지 값 범위 : 0 ~ 255
CV_16U 이미지의 값 범위 : 0 ~ 65535
CV_32F 이미지의 값 범위 : 0 ~ 1

색상 공간 코드
속성	의미	비고
BGR	Blue, Green, Red 채널	-
BGRA	Blue, Green, Red, Alpha 채널	-
RGB	Red, Green, Blue 채널	-
RGBA	Red, Green, Blue, Alpha 채널	-
GRAY	단일 채널	그레이스케일
BGR565	Blue, Green, Red 채널	16 비트 이미지
XYZ	X, Y, Z 채널	CIE 1931 색 공간
YCrCb	Y, Cr, Cb 채널	YCC (크로마)
HSV	Hue, Saturation, Value 채널	색상, 채도, 명도
Lab	L, a, b 채널	반사율, 색도1, 색도2
Luv	L, u, v 채널	CIE Luv
HLS	Hue, Lightness, Saturation 채널	색상, 밝기, 채도
YUV	Y, U, V 채널	밝기, 색상1, 색상2
BG, GB, RG	디모자이킹	단일 색상 공간으로 변경
_EA	디모자이킹	가장자리 인식
_VNG	디모자이킹	그라데이션 사용

원본 이미지 색상 공간2결과 이미지 색상 공간에 색상 공간 코드를 조합하여 사용할 수 있습니다.
예) BGR2GRAY는 Blue, Green, Red 채널 이미지를 단일 채널, 그레이스케일 이미지로 변경합니다.
'''
