# for in range 응용방법
import time


my_list = ["a", "b", "c", "d", "e", "f"]


for i in range(0, 11, 1):  # 0부터 10까지  1씩증가
    print(i)
    time.sleep(0, 5)


###for in range 실습 ,증감값(1)은 생략가능
for i in range(1, 11, 1):  # 1부터 10까지  1씩증가
    print(i)
    time.sleep(0, 5)

for i in range(0, 11, 2):  # 0이상 11미만  2씩증가
    print(i)
    time.sleep(0, 5)


for i in range(100, 89, -1):  # 100부터 90까지  거꾸로 1씩증가
    print(i)
    time.sleep(0, 5)

for i in range(10, 0, -3):  # 10부터 1까지  거꾸로 3씩증가
    print(i)
    time.sleep(0, 5)

# ##for in range 실습2
##for in range와 인덱싱 사용

my_list = ["a", "b", "c", "d", "e", "f"]

# a, b, c, d, e를 프린트해주세요
for i in range(0, 5):  # 0이상 5미만
    print(my_list[i])

# c, d, e, f 를 프린트해주세요
for i in range(2, 6):  # 2이상 6미만
    print(my_list[i])

# d, c, b를 프린트해주세요
for i in range(3, 0, -1):  # 3에서 1까지 거꾸로 1씩 증가
    print(my_list[i])

# a,c,e를 프린트해주세요
for i in range(0, 5, 2):  # 0이상 5미만 2씩 증가
    print(my_list[i])
