#coding: utf-8

score = []
for i in range(1,11):
	score.append(float(input(str(i)+"번 심사점수를 입력하시오. ")))

score.remove(max(score))
score.remove(min(score))
print("가장 큰 점수와 가장 작은 점수를 제외한 8개의 점수에 대한 평균은",round(sum(score)/8,1),"입니다.")