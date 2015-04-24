#coding: utf-8

total_charge = 0

while(True):
	s = input("사용한 시간을 시간과 분으로 입력하세요. : ")
	hour, minute = s.split(" ")

	hour = int(hour)
	minute = int(minute)

	minute += hour * 60

	if hour == 0 and minute == 0:
		print("지금까지의 이용료 총 금액은",total_charge,"원 입니다.")
		break

	if minute % 30 == 0:
		charge = (minute//30) * 1000
	else:
		charge = (minute//30 + 1) * 1000

	if hour >= 2 and hour < 3:
		charge -= charge/20
	elif hour >= 3 and hour < 5:
		charge -= charge/10
	elif hour >= 5:
		charge -= charge/5

	print(int(charge))
	total_charge += int(charge)