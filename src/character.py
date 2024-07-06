from weapon import fists

class Character:

    race = "Human"

    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.damage = damage
        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)


class Hero(Character):

    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)
         