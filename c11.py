#-*- coding: utf-8 -*-

year = input("년도를 입력하세요.")

if year % 4 == 0 and year % 400 == 0:
	print "윤년 입니다."
elif year % 4 == 0 and year % 100 == 0:
	print "윤년이 아닙니다."
elif year % 4 == 0:
	print "윤년 입니다."
else:
	print "윤년이 아닙니다."