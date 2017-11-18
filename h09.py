str = input("문자열을 입력하시오 : ")

list1 = []
list2 = []
for c in str:
    if (c.isalpha()):
        list1.append(c.lower())
        list2.append(c.lower())

list2.reverse()
print(list1, list2)
print(list1 == list2)
