import random;

coins = int(input("사용하실 코인의 개수를 입력하세요. "))
i = 0
while(coins != i):
    i += 1
    number = []
    dummy = int(input("게임 %d회 Start!! (아무 숫자나 입력하세요)" % i))
    for j in range(3):
        number.append(random.randrange(1,10))
    print("게임 결과 : %d %d %d" % (number[0], number[1], number[2]), end = " --------> " )
    for n in number:
        if (number.index(n) == 2):
            print("아쉽게도 꽝입니다..")
        elif (number.count(n) == 2):
            print("숫자 2개 일치....코인 2개 증정")
            coins += 2
            break
        elif (number.count(n) == 3):
            print("숫자 3개 일치...코인 4개 증정")
            coins += 4
            break

    print("남아 있는 코인은 %d개입니다." % (coins - i))
print("게임종료!!")
