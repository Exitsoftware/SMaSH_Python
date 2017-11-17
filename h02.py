import random

while(True):
    lotto = []
    for i in range(6):
        while(True):
            num = random.randrange(1,46)
            if (not(num in lotto)):
                break
        lotto.append(num)
    print(lotto)
    onemore = input("더 만드시겠습니까? (Y/N) ")
    if (onemore == "N"):
        break