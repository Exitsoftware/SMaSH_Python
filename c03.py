#-*- coding: utf-8 -*-

width = input("직사각형의 가로 크기를 입력하세요.")
height = input("직사각형의 세로 크기를 입력하세요.")

if width >= height * 2:
	print "좌우로 길쭉한 사각형입니다."
elif height >= width * 2:
	print "위아래로 길쭉한 사각형입니다."
elif width > height:
	print "일반적인 가로형 사각형입니다."
elif height > width:
	print "일반적인 세로형 사각형입니다."
elif width == height:
	print "정사각형입니다."