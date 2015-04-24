#coding: utf-8

monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
day_count = 0

month = int(input("월을 입력하시오. "))
day = int(input("일을 입력하시오. "))

if not (month >= 1 and month <= 12) :
	print("잘못 입력하셨습니다.")
	exit()

if not (day >= 1 and day <= monthdays[month-1]):
	print("잘못 입력하셨습니다.")
	exit()

for i in range(month-1):
	day_count += monthdays[i]

day_count += day

print("이 날짜는 1년 중",day_count,"번째 날에 해당됩니다.")