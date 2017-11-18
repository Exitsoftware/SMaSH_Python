s1 = input("첫번째 문자열? ")
s2 = input("두번째 문자열? ")

list1 = []
list2 = []
for c in s1:
    if (c.isalpha()):
        list1.append(c.lower())

for c in s2:
    if (c.isalpha()):
        list2.append(c.lower())

list1.sort()
list2.sort()

print(list1 == list2)
