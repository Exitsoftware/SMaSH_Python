#-*- coding: utf-8 -*-

birth_year = input("태어난 연도를 입력하세요.")

age = 2014 - birth_year + 1

if age >= 60:
	print "노년 입니다."
elif age >= 30 and age < 60:
	print "중년 입니다."
elif age >= 20 and age < 30:
	print "청년 입니다."
elif age >= 13 and age < 20:
	print "청소년 입니다."
elif age >= 7 and age < 13:
	print "어린이 입니다."
else:
	print "유아 입니다."