#coding: utf-8

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

while(True):
	s = input("직사각형의 가로 세로 입력")
	width, height = s.split(" ")
	width = int(width)
	height = int(height)
	if(width <= 0 or height <= 0):
		break
	else:
		if(width == height):
			count1 += 1
		elif(width >= 2*height):
			count2 += 1
		elif(width*2 <= height):
			count3 += 1
		elif(width >= height):
			count4 += 1
		elif(width <= height):
			count5 += 1


print("정사각형의 개수는",count1,"개 입니다.")
print("좌우로 길쭉한 직사각형은",count2,"개 입니다.")
print("위아래로 길쭉한 직사각혀의 개수는",count3,"개 입니다.")
print("일반적인 가로형 직사각형의 개수는",count4,"개 입니다.")
print("일반적인 세로형 직사각형의 개수는",count5,"개 입니다.")