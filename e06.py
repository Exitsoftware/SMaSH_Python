#coding: utf-8

s = input("출력하려는 행의 크기와 열의 크기를 입력하시오. ")
rows, cols = s.split(" ")
rows = int(rows)
cols = int(cols)

for i in range(1,rows+1):
	for j in range(1,cols+1):
		print(str(i*j).rjust(len(str(rows*cols))),end="\t")
	print()
