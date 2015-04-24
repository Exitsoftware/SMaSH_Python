#coding: utf-8

order = [0, 0, 0]
total_order = [0, 0, 0]
price = [10000, 6000, 3000]
total_sale = 0

print("세 종류의 제품이 있습니다.")
print("(1. 가죽 장갑 1만원, 2. 털 장갑 6천원, 3. 비닐장갑 3천원)")
print()

while(True):	

	sale = 0

	for i in range(3):
		order[i] = int(input(str(i+1)+"번 제품은 몇 개 구입하실래요? "))
		total_order[i] += order[i]
		sale += price[i]*order[i]
		total_sale += sale

	if order == [0, 0, 0]:
		print("지금까지의 총 매출 금액은",total_sale,"원 입니다.")
		break

	print("판매금액은",sale,"입니다.\n")
