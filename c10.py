
#-*- coding: utf-8 -*-

num1 = input("첫 번째 숫자를 입력하세요.")
num2 = input("두 번째 숫자를 입력하세요.")

operator = raw_input("연산기호문자 ('+', '-', '*', '/' 중 1개를 선택하세요")

if operator == '+':
	result = num1 + num2
elif operator == '-':
	result = num1 - num2
elif operator == '*':
	result = num1 * num2
elif operator == '/':
	result = num1 / num2

print "계산 결과값은",result,"입니다."