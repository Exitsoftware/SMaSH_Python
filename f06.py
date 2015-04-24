#coding: utf-8

num = []
total = 0
for i in range(5):
	num.append([])
	for j in range(3):
		newnum = int(input(str(i+1)+"0"+str(j+1)+"호에 살고 있는 사람의 숫자를 입력하시오. "))
		num[i].append(newnum)
		total += newnum

print("이 아파트에 사는 거주자는 모두",total,"명 입니다.")
