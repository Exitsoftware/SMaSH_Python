#coding: utf-8

s = input("2차 함수  y=ax^2+bx+c의 계수 a와 b, c를 입력하세요.")
a, b, c = s.split(" ")
a = int(a)
b = int(b)
c = int(c)
s = input("x좌표의 시작과 끝 값을 입력하세요.")
x_begin, x_end = s.split(" ")

for i in range(int(x_begin),int(x_end)+1):
	print("좌표("+str(i)+",",str(a*i*i+b*i+c)+")")