#coding: utf-8

number = int(input("숫자를 입력하세요."))
totalsum = 0
for i in range(number):
	totalsum += i+1
print("1부터 입력한 숫자까지의 모든 정수를 더한 값은",totalsum,"입니다.")