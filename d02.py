#coding: utf-8

num_li = []

while (True):
	number = int(input("0부터 100까지의 숫자를 입력하세요."))
	if (number >= 0 and number <= 100):
		num_li.append(number)
	else:
		break


print("입력된 숫자들 중에서 가장 큰 숫자는",max(num_li),"이고, 가장 작은 숫자는",min(num_li),"이다.")

