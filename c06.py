
#-*- coding: utf-8 -*-

kor = input("국어 점수를 입력하세요.")
eng = input("영어 점수를 입력하세요.")
math = input("수학 점수를 입력하세요.")

total = kor + eng + math
average = total / 3.0

print "입력하신 점수의 총점은",total,"이고,"
print "평균은",average,"입니다."

if average >= 90:
	print "수 입니다."
elif average >= 80 and average < 90:
	print "우 입니다."
elif average >= 70 and average < 80:
	print "미 입니다."
elif average >= 60 and average < 70:
	print "양 입니다."
else:
	print "가 입니다."