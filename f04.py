#coding: utf-8

jumsu = []

for i in range(5):
	s = input(str(i+1)+"번 학생 국어, 영어, 수학 점수를 입력하시오. ")
	kor, eng, mat = s.split(" ")
	jumsu.append([int(kor), int(eng), int(mat)])

for i in range(5):
	print(str(i+1)+"번 학생의 총점은",sum(jumsu[i]),"이고, 평균은",round(sum(jumsu[i])/3,1),"입니다.")

