class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 {} {}".format(self.name, self.hp, self.damage))


marine = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
print("유닛 이름: {}, 공격력 {}".format(tank.name, tank.damage))

wraith = Unit("레이스", 80, 5)
wraith.clocking = True
if wraith.clocking == True:
    print("{}는 클로킹 상태".format(wraith.name))


class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 공격 {}".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지 입음".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력 {}".format(self.name, self.hp))


firebat = AttackUnit("파이어뱃", 50, 16)
firebat.attack("5시")
firebat.damaged(25)
