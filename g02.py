#coding: utf-8

degrees = []
degree_name = ["냉수", "미온수", "온수", "끓는물"]
count = [0, 0, 0, 0]

for i in range(10):
	degrees.append(float(input(str(i+1)+"번 물의 온도를 입력하시오. ")))

for i in range(10):
	if degrees[i] >= 80:
		sel = 3
	elif degrees[i] >= 40 and degrees[i] < 80:
		sel = 2
	elif degrees[i] >= 25 and degrees[i] < 40:
		sel = 1
	elif degrees[i] >= 0 and degrees[i] < 25:
		sel = 0
	count[sel] += 1
	print(str(i+1)+"번 물의 온도는",degrees[i],"도 입니다.",degree_name[sel])

for i in range(4):
	print(degree_name[i],"입력 횟수 : ",count[i])

