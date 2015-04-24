#coding: utf-8

s = input("직각 삼각형의 높이와 왼쪽 여백의 크기를 입력하시오. ")
height, blank = s.split(" ")
height = int(height)
blank = int(blank)
for i in range(height):
	print((" " * blank)+(" "* (height - (i+1))) + ("*"*(i + 1)))