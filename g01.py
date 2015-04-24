#coding: utf-8

age = []

count_baby = 0
count_child = 0
count_youth = 0
count_young = 0
count_adult = 0
count_old = 0

for i in range(10):
	while(True):
		birth_year = int(input(str(i+1)+"번째 사람이 태어난 년도를 입력하시오. "))
		if(birth_year <= 2014):
			print("잘못 입력하셨습니다.")
			break

	age.append(2014 - birth_year + 1)

	if age[i] >= 60:
		count_old += 1
	elif age[i] >= 30 and age[i] < 60:
		count_adult += 1
	elif age[i] >= 20 and age[i] < 30:
		count_young += 1
	elif age[i] >= 13 and age[i] < 20:
		count_youth += 1
	elif age[i] >= 7 and age[i] < 13:
		count_child += 1
	elif age[i] < 7:
		count_baby += 1

print()

for i in range(10):
	print(str(i+1)+"번째 사람의 나이는",age[i],"입니다.")

print()

print("유아는",count_baby,"명 입니다.")
print("청소년은",count_child,"명 입니다.")
print("청년은",count_youth,"명 입니다.")
print("중년은",count_adult,"명 입니다.")
print("노년은",count_old,"명 입니다.")

