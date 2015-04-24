
#-*- coding: utf-8 -*-

num1 = input("첫 번째 숫자를 입력하세요.")
num2 = input("두 번째 숫자를 입력하세요.")
num3 = input("세 번째 숫자를 입력하세요.")

#1번 판정
if (num1 == num2) or (num1 == num3) or (num2 == num3):
	print "1번 조건 충족 : 3개의 숫자 중 적어도 두 수의 값이 같다."
#2번 판정
if (num1 > 50 and num2 > 50) or (num1 > 50 and num3 > 50) or (num2 > 50 and num3 > 50):
	print "2번 조건 충족 : 3개의 숫자 중 적어도 두 수의 크기가 모두 50 보다 크다."
#3번 판정
if (num1 == num2 + num3) or (num2 == num1 + num3) or (num3 == num1 + num2):
	print "3번 조건 충족 : 3개의 숫자 중 어떤 두 수의 합이 나머지 하나의 숫자와 같다."
#4번 판정
if (num2 % num1 == 0 and num3 % num1 == 0) or (num1 % num2 == 0 and num3 % num2 == 0) or (num1 % num3 == 0 and num2 % num3 == 0):
	print "4번 조건 충족 : 3개의 숫자 중 어떤 하나의 수로 다른 두 수를 나누면 나누어떨어지는 경우가 있다."