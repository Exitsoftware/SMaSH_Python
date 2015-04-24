#-*- coding: utf-8 -*-

m2_area = input("아파트의 분양 면적(제곱미터)을 입룍하세요.")
pyung_area = m2_area / 3.305
print "아파트의 평형은",pyung_area,"입니다."

if pyung_area >= 50:
	print "대형아파트 입니다."
elif pyung_area >= 30 and pyung_area < 50:
	print "중형아파트 입니다."
elif pyung_area >= 15 and pyung_area < 30:
	print "중소형아파트 입니다."
elif pyung_area < 15:
	print "소형아파트 입니다."