
#-*- coding: utf-8 -*-

month = input("월을 입력하세요.")
day = input("일을 입력하세요.")

day_count = 0

if month > 12 or month < 1:
	print "잘못입력하셨습니다."
else:
	for i in range(1, month):
		if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:

			if day > 31 or day < 1:
				print "잘못입력하셨습니다."
				exit()
			else:
				day_count = day_count + 31

		elif i == 2:
			if day > 28 or day < 1:
				print "잘못입력하셨습니다."
				exit()
			else:
				day_count = day_count + 28
		else:
			if day > 30 or day < 1:
				print "잘못입력하셨습니다."
				exit()
			else:
				day_count = day_count + 30

	day_count = day_count + day
	print "이 날짜는 1년 중",day_count,"번 째에 해당하는 날입니다."