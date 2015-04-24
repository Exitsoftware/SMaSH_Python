#-*- coding: utf-8 -*-

height = input("신장(cm단위)을 입력하세요.")
weight = input("체중(kg단위)을 입력하세요.")

height = height / 100.0

bmi = weight / (height * height)
print height
print bmi

if bmi >= 25:
	print "당신은 비만입니다."
else:
	print "당신은 비만이 아닙니다."
