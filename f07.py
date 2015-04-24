#coding: utf-8

num = []
line_total = [[],[],[]]
total = 0
for i in range(5):
	num.append([])
	for j in range(3):
		newnum = int(input(str(i+1)+"0"+str(j+1)+"호에 살고 있는 사람의 숫자를 입력하시오. "))
		num[i].append(newnum)
		total += newnum

for i in range(5):
	print(str(i+1)+"층에 사는 거주자는 모두",sum(num[i]),"명 입니다.")
	for j in range(3):
		line_total[j].append(num[i][j])

for i in range(3):
	print(str(i+1)+"호 라인에 사는 거주자는 모두",sum(line_total[i]),"명 입니다.")


print("이 아파트에 사는 거주자는 모두",total,"명 입니다.")
