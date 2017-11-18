str = input("문자열을 입력하시오")

count_all = len(str)
count_upper = 0
count_lower = 0
count_space = 0
count_number = 0
count_etc = 0

for c in str:
    if (c.isupper()):
        count_upper += 1
    elif (c.islower()):
        count_lower += 1
    elif (c.isspace()):
        count_space += 1
    elif (c.isdigit()):
        count_number += 1
    else:
        count_etc += 1

print("총 문자 개수: ", count_all)
print("대문자 개수: ", count_upper)
print("소문자 개수: ", count_lower)
print("공백 개수: ", count_space)
print("숫자 개수: ", count_number)
print("기타 문재 개수: ", count_etc)
