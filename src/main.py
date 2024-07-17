import os
from character import Hero, Enemy, Warrior, Warlock
from weapon import short_bow, iron_sword

class_mapping = {
    'wr': Warrior,
    'wl': Warlock
}

enemy = Warlock(name="Warlock")

print("Choose a class for your hero:")
class_chosen = input("- Press 'wr' for Warrior, 'wl' for Warlock: \n").lower()

print("Choose a name for your hero:")
name_choosen = input()

hero_class = class_mapping.get(class_chosen, Warrior)
hero = hero_class(name=name_choosen)

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