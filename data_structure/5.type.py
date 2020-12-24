from random import *
menu = {"커피", "우유", "주스"}
print(menu, type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))

users = range(1, 21)
print(type(users))
users = list(users)
print(users)
shuffle(users)
print(users)
winners = sample(users, 4)
print(winners)
