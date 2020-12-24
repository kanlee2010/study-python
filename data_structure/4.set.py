# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

my_set2 = {1, 4, 5}
print(my_set & my_set2)
print(my_set.intersection(my_set2))
print(my_set | my_set2)
print(my_set.union(my_set2))
print(my_set - my_set2)
print(my_set.difference(my_set2))

my_set.add(10)
print(my_set)
my_set.remove(3)
print(my_set)
