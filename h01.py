import random
answer = random.randrange(1,101)

count = 0
while(True):
    count = count + 1
    number_try = int(input("1부터 100까지의 숫자 하나를 맞춰보세요 "))
    if (answer > number_try):
        print("좀 더 큰 수 입니다.")
    elif (answer < number_try):
        print("좀 더 작은 수입니다.")
    else:
        break
print("%d번 만에 숫자를 맞추셨습니다." % count)
