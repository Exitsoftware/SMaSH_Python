import random

score = [[0,0,0],[0,0,0]]

while True:
    my_finger = int(input("가위(1), 바위(2), 보(3)를 입력하세요. "))
    com_finger = random.randrange(1,4)

    if (my_finger == 0):
        break

    if (com_finger == 1):
        print("컴퓨터가 낸 것은 가위입니다.", end=" -------> ")
    elif (com_finger == 2):
        print("컴퓨터가 낸 것은 바위입니다.", end=" -------> ")
    elif (com_finger == 3):
        print("컴퓨터가 낸 것은 보입니다.", end=" -------> ")

    if ((my_finger - com_finger) == 0):
        print("비김~")
        score[0][1] += 1
        score[1][1] += 1
    elif (my_finger == 1):
        if (com_finger == 2):
            print("컴퓨터 승!")
            score[0][0] += 1
            score[1][2] += 1
        elif (com_finger == 3):
            print("사용자 승!")
            score[0][2] += 1
            score[1][0] += 1
    elif (my_finger == 2):
        if (com_finger == 3):
            print("컴퓨터 승!")
            score[0][0] += 1
            score[1][2] += 1
        elif (com_finger == 1):
            print("사용자 승!")
            score[0][2] += 1
            score[1][0] += 1
    elif (my_finger == 3):
        if (com_finger == 1):
            print("컴퓨터 승!")
            score[0][0] += 1
            score[1][2] += 1
        elif (com_finger == 2):
            print("사용자 승!")
            score[0][2] += 1
            score[1][0] += 1


print("컴퓨터 : 이긴 횟수는 %d회, 진 횟수 %d회, 비긴 횟수는 %d 입니다." % (score[0][0], score[0][2], score[0][1]))
print("사용자 : 이긴 횟수는 %d회, 진 횟수 %d회, 비긴 횟수는 %d 입니다." % (score[1][0], score[1][2], score[1][1]))
