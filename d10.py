#coding: utf-8

s = input("2개의 숫자를 입력하세요.")
num1, num2 = s.split(" ")
num1 = int(num1)
num2 = int(num2)
li = []
for i in range(1, 100//num1):
	li.append(i*num1)
for i in range(1, 100//num2):
	li.append(i*num2)
for i in range(1, 100//num1*num2):
	if num1*num2*i in li:
		li.remove(i*num1*num2)
li.sort()
for i in range(len(li)):
	if i == len(li)-1:
		print(li[i])
	else:
		print(li[i],end=", ")