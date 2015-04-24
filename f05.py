#coding: utf-8

bmilist = []
count = 0
for i in range(10):
	s = input(str(i+1)+"번째 사람의 신장(cm)과 체중(kg)을 입력하시오. ")
	height, weight = s.split()
	bmilist.append([int(height)/100,int(weight)])

print("")

for i in range(len(bmilist)):
	bmi = bmilist[i][1] / bmilist[i][0]**2
	if(bmi >= 25):
		count += 1
		print(str(i+1)+"번째 사람은 비만 입니다.")

print("")

print("총",count,"명의 사람이 비만입니다.")