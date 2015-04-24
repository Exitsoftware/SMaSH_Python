#coding: utf-8

number = []

print("1부터 100사이의 숫자를 입력하시오.")
for i in range(10):
	while(True):
		newnum = int(input(str(i+1)+"번째 숫자를 입력하시오. "))
		if not newnum in number:
			number.append(newnum)
			break
		else:
			print("잘못 입력하셨습니다. 다시 입력하세요.")

for i in range(10):
	print(str(i+1)+"번째 숫자는",number[i],"입니다.")
