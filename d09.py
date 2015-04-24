#coding: utf-8

while(True):
	dan = int(input("입력하고 싶은 구구단의 단 수를 입력하시오(2-9) : "))
	if(dan >= 2 and dan <= 9):
		for i in range(1,10):
			print(dan,"x",i,"=",i*dan)
		break
	else:
		print("잘못 입력하셨습니다.")
