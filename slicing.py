##또 다른 슬라이싱 방법#전체값 출력
my_list = ["a", "b", "c", "d", "e", "f"]
new_list = my_list[0:-1:1]
# new_list = my_list[:]
# new_list = my_list[::-1]
# print(new_list)

# 응용편
my_list = ["가", "나", "다", "라"]

print(my_list[0])  # 가
print(my_list[1])  # 나
print(my_list[2])  # 다
print(my_list[3])  # 라
print(my_list[:])  # 전체출력
print(my_list[0:2])  # 0이상 2미만
print(my_list[::-1])  # 거꾸로


# 슬라이싱 실습
my_list = ["a", "b", "c", "d", "e", "f"]
print(my_list[0:5])  # 1번문제
# print(my_list[:-1])#1번문제

print(my_list[2:6])  # 2번문제

print(my_list[3:0:-1])  # 3번문제

# 0이상 5미만 증감은 2
print(my_list[0:5:2])  # 4번문제
print(my_list[::2])  # 4번문제

print(my_list[-1])  # 번외: f 출력
