from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Нанесен удар мечом")
        print("Монстр побежден!")

class Bow(Weapon):
    def attack(self):
        print("Произведен выстрел из лука")
        print("Монстр побежден!")

class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        self.weapon.attack()

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print(f"Боец выбрал {new_weapon.name}")


class Monster():
    def __init__(self):
        pass


sword = Sword('меч')
bow = Bow('лук')
fighter = Fighter(sword)
fighter.fight()
fighter.change_weapon(bow)
fighter.fight()
fighter.change_weapon(sword)
fighter.fight()