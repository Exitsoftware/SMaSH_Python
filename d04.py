#coding: utf-8

count_all = int(input("가족이 몇 명인지 입력하세요"))
count_young = 0

for i in range(count_all):
	birth_year = int(input("태어난 연도를 입력하세요."))
	age = 2014 - birth_year + 1
	if (age < 20):
		count_young += 1
print("가족들 중 미성년자는",count_young,"명 입니다.")