from weapon import fists, short_bow, wooden_sword
from health_bar import HealthBar

class Character:

    def __init__(self, name: str):
        self.name = name

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}")

class Warrior(Character):

    health = 150
    weapon = wooden_sword

    def __init__(self, name: str) -> None:
        super().__init__(name=name)
        self.name = "(wr)" + name 
        self.weapon = self.weapon
        self.health = self.health
        self.health_max = self.health
        self.health_bar = HealthBar(self, color='green')

class Warlock(Character):

    health = 120
    weapon = short_bow

    def __init__(self, name: str) -> None:
        super().__init__(name=name)
        self.weapon = self.weapon
        self.health = self.health
        self.health_max = self.health
        self.health_bar = HealthBar(self, color='red')

class Hero(Character):

    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color='green')
    
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f'{self.name} eqquipped a(n) {self.weapon.name}!')
        
    def drop(self) -> None:
        print(f'{self.name} dropped the {self.weapon.name}')
        self.weapon = self.default_weapon

class Enemy(Character):

    health = 120

    def __init__(self, name: str, 
                 health: int,
                 weapon) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color='red')
