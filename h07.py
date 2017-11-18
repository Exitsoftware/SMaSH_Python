import math

number = list(map(int, input("1부터 100사이의 숫자 10개를 입력하세요 ").split(" ")))

total = sum(number)
avg = total / len(number)

print("입력하신 10개의 수의 총합은 %d, 평균은 %.1f입니다." % (total, avg))
print("분산은 다음과 같습니다.")

bunsan = []
for n in number:
    b = pow(n - avg, 2)
    bunsan.append(b)
    print("%.1f" % b, end =" ")
bunsan_avg = sum(bunsan)/len(bunsan)
print("\n분산의 평균은 %.1f이고 표준편차는 %.1f입니다." % (bunsan_avg, math.sqrt(bunsan_avg)))
