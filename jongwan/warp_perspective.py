import numpy as np
import cv2

src = cv2.imread("Image/harvest.jpg", cv2.IMREAD_COLOR)
height, width, channel = src.shape

srcPoint=np.array([[0, 200], [400, 200], [500, 500], [500, 100]], dtype=np.float32)
dstPoint=np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)
#원본 이미지에서 4점 변환할 srcPoint와 결과 이미지의 위치가 될 dstPoint를 선언한다
#좌표의 순서는 좌상, 우상, 우하, 좌하 순서입니다. numpy 형태로 선언하며, 좌표의 순서는 원본 순서와 결과 순서가 동일해야한다
#Tip : dtype을 float32 형식으로 선언해야 사용할 수 있다.

matrix = cv2.getPerspectiveTransform(srcPoint, dstPoint)
#기하학적 변환을 위하여 cv2.getPerspectiveTransform(원본 좌표 순서, 결과 좌표 순서)를 사용하여 matrix를 생성한다
#다음과 같은 형식으로 매트릭스가 생성된다
'''[[-2.88000000e+01 -9.60000000e+00  1.05600000e+04]
    [-4.44089210e-15 -2.15400000e+01  4.30800000e+03]
    [-1.77809156e-17 -2.00000000e-02  1.00000000e+00]]'''
dst = cv2.warpPerspective(src, matrix, (width, height))
#cv2.warpPerspective(원본 이미지, 매트릭스, (결과 이미지 너비, 결과 이미지 높이))를 사용하여 이미지를 변환할 수 있다
#저장된 매트릭스 값을 사용하여 이미지를 변환
#이외에도, 보간법, 픽셀 외삽법을 추가적인 파라미터로 사용할 수 있다

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()