number = list(map(int, input("2에서 9까지 숫자 5개를 입력하세요").split(" ")))
number.sort()
max_a, max_b = number[3], number[4]
min_a, min_b = number[0], number[1]

max = max(pow(max_a, max_b), pow(max_b, max_a))
min = min(pow(min_a, min_b), pow(min_b, min_a))

if (pow(max_a, max_b) == max):
    print("가장 큰 수는 %d의 %d승인 %d입니다." % (max_a, max_b, max))
else:
    print("가장 큰 수는 %d의 %d승인 %d입니다." % (max_b, max_a, max))


if (pow(min_a, min_b) == min):
    print("가장 큰 수는 %d의 %d승인 %d입니다." % (min_a, min_b, min))
else:
    print("가장 큰 수는 %d의 %d승인 %d입니다." % (min_b, min_a, min))
