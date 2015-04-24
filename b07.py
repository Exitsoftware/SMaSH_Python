#-*- coding: utf-8 -*-

megabytes = input("파일 용량을 메가바이트 단위로 입력하세요.")
bytes = megabytes * 1024 * 1024
usb2 = raw_input("usb포트가 2.0이면 'Y', 아니면 'N'을 입력하세요.")
if usb2 == 'Y':
	time = bytes / 60000000
	print "파일전송 속도는",time,"초 입니다."
elif usb2 == 'N':
	time = bytes / 15000000
	print "파일전송 속도는",time,"초 입니다."
else:
	print "잘못입력하셨습니다."