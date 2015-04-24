#coding: utf-8

total_charge = 0

while(True):
	kind = int(input("부동산 거래종류(1.매매 2.임대 0.계산종료)를 입력하세요. : "))

	if kind == 0:
		print("지금까지의 수수료 총액은",int(total_charge),"원 입니다.")
		break
	
	money = int(input("부동산 거래금액(원)을 입력하세요. : "))

	if kind == 1:
		if money >= 200000000:
			charge = money/1000 * 4
		elif money >= 50000000 and money < 200000000:
			charge = money/1000 * 5
			if charge >= 800000:
				charge = 800000
		elif money < 50000000:
			charge = money/1000 * 6
			if charge >= 250000:
				charge = 250000

	elif kind == 2:
		if money >= 100000000:
			charge = money/1000 * 3
		elif money >= 50000000 and money < 100000000:
			charge = money/1000 *4
			if charge >= 300000:
				charge = 300000
		elif money >= 20000000 and money < 50000000:
			charge = money/1000 * 5
			if charge >= 200000:
				charge = 200000
		elif money < 20000000:
			charge = money/1000 * 5
			if charge >= 70000:
				charge = 70000
	
	total_charge += charge
	print("이에 대한 중개 수수료는",int(charge),"원 입니다.")



