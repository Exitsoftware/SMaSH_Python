#coding: utf-8

jumsu = []
class_score = []
class_name = ["국어","영어","수학"]


for i in range(5):
	s = input(str(i+1)+"번 학생의 국어, 영어, 수학 점수는? ")
	kor, eng, mat = s.split(" ")
	jumsu.append([int(kor),int(eng),int(mat)])

print()
print("1) 각 과목별 총점과 평균 점수")
for i in range(3):
	grade_sum = 0
	for j in range(5):
		grade_sum += jumsu[j][i]

	print(class_name[i],"과목 총점은",grade_sum,"평균은 ",round(grade_sum/5,1),"입니다")

print()
print("2) 각 과목별 총점과 평균 점수")
for i in range(5):
	average = round(sum(jumsu[i])/3,1)
	if (average >= 90):
		grade = 'A'
	elif (average >= 80 and average < 90):
		grade = 'B'
	elif (average >= 70 and average < 80):
		grade = 'C'
	elif (average >= 60 and average < 70):
		grade = 'D'
	elif (average < 60):
		grade = 'F'
	print(str(i+1)+"번 학생 점수 : 총점",sum(jumsu[i]),"평균",average,"등급",grade )