
#-*- coding: utf-8 -*-

income = input("연봉을 (원 단위)로 입력하세요.")
income = income / 100;

if income >= 80000000:
	tax = income * 37
elif income >= 40000000 and income < 80000000:
	tax = income * 28
elif income >= 10000000 and income < 40000000:
	tax = income * 19
else:
	tax = income * 9.5

print "연봉 금액에 대한 소득세는",'%.0f'%tax,"원 입니다."