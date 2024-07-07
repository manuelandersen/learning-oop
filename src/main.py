import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword

hero = Hero(name="Hero", health=100)
hero.equip(weapon=iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow )

while True:

    os.system("cls" if os.name == "nt" else "clear")

    #hero.attack(enemy)
    #enemy.attack(hero)

    hero.attack(enemy)
    if enemy.health == 0:
        print(f"{enemy.name} has been defeated!")
        break

    enemy.attack(hero)
    if hero.health == 0:
        print(f"{hero.name} has been defeated!")
        break

    hero.health_bar.draw()
    enemy.health_bar.draw()

    if input("Press Enter to continue, or 'q' to quit: ").lower() == 'q': break