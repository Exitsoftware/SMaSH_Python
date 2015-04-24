#-*- coding: utf-8 -*-

days = input("날 수를 입력하세요.")
seconds = days * 24 * 60 * 60
print "날 수에 해당되는 시간은",seconds,"초 입니다."
if seconds >= 1000000:
	m_count = seconds / 1000000
	print "100만초가",m_count,"번이나 포함됩니다."

