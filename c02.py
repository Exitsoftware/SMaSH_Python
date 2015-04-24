#-*- coding: utf-8 -*-

input_degree = input("물의 온도를 입력해주세요.")

if input_degree >= 80:
	print "끓는 물입니다."
elif input_degree >= 40 and input_degree < 80:
	print "온수 입니다."
elif input_degree >= 25 and input_degree < 40:
	print "미온수 입니다."
elif input_degree >= 0 and input_degree < 25:
	print "냉수 입니다."
else:
	print "잘못입력하셨습니다."