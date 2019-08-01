import csv
import os
import json


file_read = open("./data/방사능.csv",'r',encoding='utf-8') 							#지역코드 넣기전 파일
file_output = open("./data/방사능_RegionCode.csv","a",encoding="utf-8",newline='')	#지역코드 넣은후 파일
region_code = open("region_code.txt","r",encoding="utf-8")


rdr = csv.reader(file_read)
wr = csv.writer(file_output)
RegionCode_dict = json.load(region_code)

regions = list(RegionCode_dict.keys())

cnt = 0
wr.writerow(['\ufeff지역', '지역명', '지역코드','μSv/h', 'μR/h', '상태'])
for row in rdr:	#지역코드 넣기
	if cnt == 0:
		cnt +=1
		continue

	chk = 0
	line_RegionCode = row

	for i in regions:
		if i in row[1]:	#지역명 열을 살펴봐서 그지역에 지역 코드가있는지 체크 
			line_RegionCode.insert(2,RegionCode_dict[i])		
			chk = 1

	if chk !=1:	#지역코드가 없으면 NULL을 삽입
		line_RegionCode.insert(2,"NULL")		

	wr.writerow(line_RegionCode)
	
	
