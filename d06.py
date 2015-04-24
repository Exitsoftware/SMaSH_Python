#coding: utf-8

count1 = 0
count2 = 0
count3 = 0
count4 = 0

for i in range(10):
	m2_area = float(input("아파트의 분양 면적(제곱미터)을 입력하세요."))
	pyung_area = round(m2_area / 3.305,1)
	print("---> 이 아파트의 평형은,",pyung_area,"입니다.")
	if pyung_area >= 50:
		count4 += 1
	elif pyung_area >= 30 and pyung_area < 50:
		count3 += 1
	elif pyung_area >= 15 and pyung_area < 30:
		count2 += 1
	elif pyung_area < 15:
		count1 += 1

print("소형 아파트의 개수는",count1,"개 입니다.")
print("중소형 아파트의 개수는",count2,"개 입니다.")
print("중형 아파트의 개수는",count3,"개 입니다.")
print("대형 아파트의 개수는",count4,"개 입니다.")
