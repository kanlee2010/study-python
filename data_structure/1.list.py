subway = ["유재석", "조세호", "박명수"]
print(subway)
print(subway.index("조세호"))
subway.append("하하")
print(subway)
subway.insert(1, "정형돈")
print(subway)
print(subway.pop())
subway.append("유재석")
print(subway.count("유재석"))
subway.sort()
print(subway)
subway.reverse()
print(subway)
shuffle(subway)
subway.clear()
print(subway)

mixed_list = ["조세호", 20, True]
num_list = [1, 2, 3]
print(mixed_list)
mixed_list.extend(num_list)
print(mixed_list)
