class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def move(self, location):
        print(self.name, location, "으로 이동합니다")


class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        # Unit.__init__(self, name, hp) # 다중 상속의 경우 명시적으로 지정해야 됨
        super().__init__(name, hp)
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 공격 {}".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지 입음".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력 {}".format(self.name, self.hp))


class FyingUnit(Unit):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage

    def fly(location):
        print(self.name, location, "으로 날아 갑니다")


firebat = AttackUnit("파이어뱃", 50, 16)
firebat.attack("5시")
firebat.damaged(25)

wraith = FyingUnit("레이스", 80, 5)

attack_units = []
attack_units.append(wraith)
attack_units.append(firebat)

print("총", len(attack_units), "개 유닛이 있습니다")
for unit in attack_units:
    unit.move("1시")
    if isinstance(unit, AttackUnit):
        unit.attack("1시")
