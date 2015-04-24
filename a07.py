#-*- coding: utf-8 -*-

gigabytes = input("파일 용량을 기가바이트 단위로 입력하세요.")
megabytes = gigabytes * 1024
kilobytes = megabytes * 1024
bytes = kilobytes * 1024
print "입력하신 용량은"
print " ",megabytes,"메가바이트"
print " ",kilobytes,"킬로바이트"
print " ",bytes,"바이트 입니다."