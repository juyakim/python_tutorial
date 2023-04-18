# ####리스트 실습 4/18

# my_list = [‘a’, ‘b’, ‘c’]
# 슬라이싱을 해서 new_list에 ‘b’, ‘c’만 저장

##my answer
my_list = ["a", "b", "c"]
new_list = my_list[1][2]
print(new_list)


##solution
my_list = ["a", "b", "c"]
new_list = my_list[1:3]  # 1이상 3미만
print(new_list)


# 거꾸로해서 ‘c’, ‘b’, ‘a’ 가 저장되게!

# my answer
my_list = ["a", "b", "c", "d", "e", "f"]
new_list = my_list[2::-1]
print(new_list)
