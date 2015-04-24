#coding: utf-8

s = input("1차 함수  y=ax+b의 계수와 a와 b를 입력하세요.")
a, b = s.split(" ")
a = int(a)
b = int(b)
s = input("x좌표의 시작과 끝 값을 입력하세요.")
x_begin, x_end = s.split(" ")

for i in range(int(x_begin),int(x_end)+1):
	print("좌표("+str(i)+",",str(a*i+b)+")")