#-*- coding: utf-8 -*-
num1, num2 = raw_input("숫자 두개를 입력하세요.").split()
num1 = int(num1)
num2 = int(num2)
if num1 == num2:
	print "둘은 같습니다."
else:
	print "둘은 같지 않아요."