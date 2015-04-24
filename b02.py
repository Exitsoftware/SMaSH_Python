#-*- coding: utf-8 -*-

input_degre = input("온도를 입력하세요.")
kind = raw_input("입력하신 온도가 섭씨면 C, 화씨면 F를 입력하세요.")
if kind == 'C':
	output_degre = input_degre * 1.8 + 32
	print "변환된 온도는",output_degre,"도 입니다."
elif kind == 'F':
	output_degre = (input_degre - 32) / 1.8
	print "변환된 온도는",output_degre,"도 입니다."
else:
	print "잘못입력하셨습니다."