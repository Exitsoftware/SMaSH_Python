#coding: utf-8

mode = int(input("구구단의 출력모드(1: 홀수단, 2: 짝수단)를 입력하시오. "))
col = int(input("한 줄에 출력할 갯수를 입력하시오. "))

if mode == 1:
	for i in range(2,10):
		if i%2 == 1:
			for j in range(1,10):
				print(i,"X",j,"=",i*j, end="\t")
				if j%col == 0:
					print("")
			print("")

else:
	for i in range(2,10):
		if i%2 == 0:
			for j in range(1,10):
				print(i,"X",j,"=",i*j, end="\t")
				if j%col == 0:
					print("")
			print("")
