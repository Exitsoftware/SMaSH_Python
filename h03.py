import random

lotto_com = []
for i in range(6):
    while(True):
        num = random.randrange(1, 46)
        if (not(num in lotto_com)):
            break
    lotto_com.append(num)
    
lotto_user = []
for i in range(6):
    while(True):
        num = int(input("원하는 %d번째 로또 숫자를 입력하세요" % (i+1)))
        if (1 <= num and num <= 45):
            if (not(num in lotto_user)):
                break
        print("=> 잘못 입력하셨습니다.")
    lotto_user.append(num)

count = 0
print("이번 주의 로또 당첨 번호는 ", end="")
for num in lotto_com:
    print(num, end=" ")
    if (num in lotto_user):
        count = count + 1
print("입니다.\n")
print("일치하는 로또 번호는 %d개 입니다." % count)

    
