#coding: utf-8

num_li = []
count = 0

while (True):
	number = int(input("0부터 100까지의 숫자를 입력하세요."))
	if (number >= 0 and number <= 100):
		num_li.append(number)
		count +=1
	else:
		break


average = sum(num_li)//count

print("입력한",count,"개의 숫자들의 합은",sum(num_li),"이고, 평균은",average,"이다.")

