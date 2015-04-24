
#-*- coding: utf-8 -*-

num1 = input("첫 번째 숫자를 입력하세요.")
num2 = input("두 번째 숫자를 입력하세요.")
num3 = input("세 번째 숫자를 입력하세요.")

if num1 >= num2 and num1 >= num3:
	max_num = num1
elif num2 >= num1 and num2 >= num3:
	max_num = num2
elif num3 >= num1 and num3 >= num2:
	max_num = num3

if num1 <= num2 and num1 <= num3:
	min_num = num1
elif num2 <= num1 and num2 <= num3:
	min_num = num2
elif num3 <= num1 and num3 <= num2:
	min_num = num3

print "가장 큰 수는",max_num,"이고, 가장 작은 수는",min_num,"입니다."