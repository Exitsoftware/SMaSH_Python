
#-*- coding: utf-8 -*-

kor = input("국어 점수를 입력하세요.")
eng = input("영어 점수를 입력하세요.")
math = input("수학 점수를 입력하세요.")

total = kor + eng + math
average = total / 3.0;

print "입력하신 점수의 총점은",total,"점 이고,"
print "평균은",'%.1f'%average,"점 입니다."