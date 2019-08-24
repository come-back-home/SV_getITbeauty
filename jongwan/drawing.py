import numpy as np
import cv2

src = np.zeros((768, 1366, 3), dtype = np.uint8)

cv2.line(src, (100, 100), (1200, 100), (0, 0, 255), 3, cv2.LINE_AA)
#cv2.line(이미지, (x1, y1), (x2, y2), (B, G, R), 두께, 선형 타입)을 이용하여 선을 그린다
#(x1, y1)과 (x2, y2)가 연결된 (B, G, R) 색상, 두께 굵기의 선을 그릴 수 있다
#선형 타입은 선의 연결성을 의미

cv2.circle(src, (300, 300), 50, (0, 255, 0), cv2.FILLED, cv2.LINE_4)
#cv2.circle(이미지, (x, y), 반지름, (B, G, R), 두께, 선형 타입)을 이용하여 원을 그린다
#(x, y) 중심점을 가지는 반지름 크기로 설정된 (B, G, R) 색상, 두께 굵기의 원을 그릴 수 있다
#Tip : 내부를 채우는 경우, 두께를 cv2.FILLED을 사용하여 내부를 채울 수 있다

cv2.rectangle(src, (500, 200), (1000, 400), (255, 0, 0), 5, cv2.LINE_8)
#cv2.rectangle(이미지, (x1, y1), (x2, y2), (B, G, R), 두께, 선형 타입)을 이용하여 사각형을 그릴 수 있다
#(x1, y1)의 좌측 상단 모서리와 (x2, y2)의 우측 하단 모서리가 연결된 (B, G, R) 색상, 두께 굵기의 사각형을 그릴 수 있다

cv2.ellipse(src, (1200, 300), (100, 50), 0, 90, 180, (255, 255, 0), 2)
#cv2.ellipse(이미지, (x, y), (lr, sr), 각도, 시작 각도, 종료 각도, (B, G, R), 두께, 선형 타입)을 이용하여 타원을 그릴 수 있다
#(x, y)의 중심점을 가지며 중심에서 가장 먼 거리를 가지는 lr과 가장 가까운 거리를 가지는 sr의 타원을 각도만큼 기울어진 타원를 생성
#시작 각도와 종료 각도를 설정하여 호의 형태로 그리며 (B, G, R) 색상, 두께 굵기의 타원을 그릴 수 있다
#Tip : 선형 타입은 설정하지 않아도 사용할 수 있다

pts1 = np.array([[100, 500], [300, 500], [200, 600]])
pts2 = np.array([[600, 500], [800, 500], [700, 600]])
#poly 함수를 사용하는 경우, numpy 형태로 저장된 위치 좌표들이 필요하다
#n개의 점이 저장된 경우, n각형을 그릴 수 있다

cv2.polylines(src, [pts1], True, (0, 255, 255), 2)
#cv2.polylines(이미지, [위치 좌표], 닫힘 유/무, (B, G, R), 두께, 선형 타입 )을 이용하여 다각형을 그릴 수 있다
#[위치 좌표]들의 지점들을 가지며 시작점과 도착점이 연결되어있는지 닫힘 유/무를 설정하여 (B, G, R) 색상, 두께 굵기의 다각형을 그릴 수 있다

cv2.fillPoly(src, [pts2], (255, 0, 255), cv2.LINE_AA)
#cv2.fillPoly(이미지, [위치 좌표], (B, G, R), 두께, 선형 타입 )을 이용하여 내부가 채워진 다각형을 그릴 수 있다
#[위치 좌표]들의 지점들을 가지며 (B, G, R) 색상, 두께 굵기의 내부가 채워진 다각형을 그릴 수 있다

cv2.putText(src, "JONGWANHONG", (900, 600),cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 3)
#cv2.putText(이미지, 문자, (x, y), 글꼴, 글자 크기, (B, G, R), 두께, 선형 타입)을 이용하여 문자를 그릴 수 있다
#문자 내용을 가지는 문자열을 (x, y) 위치에 표시합니다. 글꼴와 글자 크기를 가지며 (B, G, R) 색상, 두께 굵기의 문자를 그릴 수 있다
#Tip : 문자의 위치는 좌표의 좌측 하단을 기준으로 글자가 생성된다

cv2.imshow("src", src)

cv2.waitKey(0)
cv2.destroyAllWindows()

#shift : 좌표를 Shift(비트 연산)만큼 이동시켜 표시
#offset : 좌표를 (x, y)만큼 이동시켜 표시
'''선형 타입 종류
속성 	의미
cv2.FILLED 	내부 채우기
cv2.LINE_4 	4점 이웃 연결
cv2.LINE_8 	8점 이웃 연결
cv2.LINE_AA 	AntiAlias



글꼴 종류
속성 	                            의미 	
cv2.FONT_HERSHEY_SIMPLEX 	보통 크기의 산세리프 글꼴 	
cv2.FONT_HERSHEY_PLAIN   	작은 크기의 산세리프 글꼴 	
cv2.FONT_HERSHEY_DUPLEX 	보통 크기의 산세리프 글꼴 	
cv2.FONT_HERSHEY_COMPLEX 	보통 크기의 세리프 글꼴 	
cv2.FONT_HERSHEY_TRIPLEX 	보통 크기의 세리프 글꼴 	
cv2.FONT_HERSHEY_COMPLEX_SMALL 	작은 크기의 손글씨 글꼴 	
cv2.FONT_HERSHEY_SCRIPT_SIMPLEX 	보통 크기의 손글씨 글꼴 	
cv2.FONT_HERSHEY_SCRIPT_COMPLEX 	보통 크기의 손글씨 글꼴 
cv2.FONT_ITALIC                 	기울임 꼴 	
'''