#coding: utf-8

num = []
for i in range(10):
	num.append(int(input(str(i+1)+"번째 수를 입력하시오.")))

second = sorted(num,reverse=True)[1]
second_max_index = num.index(sorted(num,reverse=True)[1])+1
print("두 번째로 큰 수는",second_max_index,"번째 수",second,"입니다.")
