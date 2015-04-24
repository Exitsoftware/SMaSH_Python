#coding: utf-8

jumsu = [[],[],[]]

for i in range(5):
	s = input(str(i+1)+"번 학생 국어, 영어, 수학 점수를 입력하시오. ")
	kor, eng, mat = s.split(" ")
	jumsu[0].append(int(kor))
	jumsu[1].append(int(eng))
	jumsu[2].append(int(mat))

print("국어의 총점은",sum(jumsu[0]),"이고, 평균은",round(sum(jumsu[0])/5,1),"입니다.")
print("영어의 총점은",sum(jumsu[1]),"이고, 평균은",round(sum(jumsu[1])/5,1),"입니다.")
print("수학의 총점은",sum(jumsu[2]),"이고, 평균은",round(sum(jumsu[2])/5,1),"입니다.")
