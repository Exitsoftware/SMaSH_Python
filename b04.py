#-*- coding: utf-8 -*-

m2_area = input("아파트의 분양면적(제곱미터)를 입력하세요.")
pyung_area = m2_area / 3.305
print "아파트의 평형은",pyung_area,"이고, "
if pyung_area < 30:
	print "30평 미만이므로 작은 아파트입니다."
else:
	print "30평 이상이므로 큰 아파트입니다."