#-*- coding: utf-8 -*-

kor = input("국어 점수를 입력하세요.")
eng = input("영어 점수를 입력하세요.")
math = input("수학 점수를 입력하세요.")

total = kor + eng +math
average = total / 3.0;
print "입력하신 점수의 총점은",total,"점이고,"
print "평균은",'%.1f'%average,"점입니다."

if kor >= 90:
	print "국어 점수가 우수합니다."
if eng >= 90:
	print "영어 점수가 우수합니다."
if math >= 90:
	print "수학 점수가 우수합니다."