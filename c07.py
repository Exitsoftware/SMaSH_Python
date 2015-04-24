#-*- coding: utf-8 -*-

megabytes = input("파일 용량을 메가바이트 단위로 입력하세요.")
bytes = megabytes * 1024 * 1024
kind = input("전송방식을 1. Wi-Fi, 2. Bluetooth, 3. LTE, 4.USB 에서 선택하여 입력하세요.")

if kind == 1:
	time = bytes / 1500000.0
elif kind == 2:
	time = bytes / 300000.0
elif kind == 3:
	time = bytes / 1000000.0
elif kind == 4:
	time = bytes / 60000000.0
else:
	print "잘못 입력하셨습니다."

print "파일 전송 시간은",'%.1f'%time,"초 입니다."
