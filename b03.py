#-*- coding: utf-8 -*-

width = input("직사각형의 가로 크기를 입력하세요.")
height = input("직사각형의 세로 크기를 입력하세요.")
area = width * height
print "직사각형의 넓이는",area,"이고,"

if width == height:
	print "정사각형입니다."
else:
	print "정사각형이 아닙니다."
