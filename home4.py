from random import randint
from enum import Enum

class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4

    def __str__(self):
        return self.CRITICAL_DAMAGE


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def hit(self, boss, heroes):
        pass

    def __str__(self):
        return f'{self.__name} health: {self.health} [{self.damage}]'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def hit(self, boss, heroes):
        for hero in heroes:
            if hero.health < 0:
                if boss.health > 0 and hero.health > 0:
                    hero.health = hero.health - boss.damage


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def apply_super_ability(self, boss, heroes):
        pass

    def hit(self, boss):
        if boss.health > 0 and self.health > 0:
            boss.health = boss.health - self.damage

    # def rr(self, heroes):


# -------------Персонажы-------------------------------------------------------------


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "BOOST")

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.damage = hero.damage + 5


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "REVENGE")

    def apply_super_ability(self, boss, heroes):
        if self.health - boss.damage:
            self.damage = self.damage + (boss.damage / 12)
        else:
            boss.damage = boss.damage




class Golem(Hero):
    def __init__(self, name, health, damage, protection=0):
        super().__init__(name, health, damage, "PROTECTION")
        self.__protection = protection

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                self.__protection = boss.damage // 5
                if boss.damage >= 1:
                    hero.health = hero.health + self.__protection
                else:
                    hero.health = hero.health - boss.damage

#
# class Witcher(Hero):
#     def __init__(self, name, health, damage):
#         super().__init__(name, health, damage, "SAVIOR")
#
#     def apply_super_ability(self, boss, heroes):
#         self.damage = 0
#         for hero in heroes:
#             if hero.health >= 0:
#                 self.health = hero.health
#                 self.health = 0
#             else:
#                 self.health = 0

class Witcher(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, 'PIECE OF LIGHT')

    def apply_super_power(self, boss, heroes):
        if boss.health > 0 and self.health > 0:
            for h in heroes:
                if h.health == 0:
                    h.health = self.health
                    self.health = 0
                    print(f'-------{self.name} revive {h.name}-------')
                    break




class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "HACKER")

    def apply_super_ability(self, boss, heroes):
        rnd = randint(10, 30)
        for hero in heroes:
            boss.health - rnd
            hero.health + rnd




round_number = 0


def print_statistics(boss, heroes):
    print(" ")
    print(f'{round_number} ROUND -----------------')
    print(boss)
    print("---------VS--------")
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print(">>>>>>>>><<<<<<<<<<")
        print("Heroes won!!!")
        print(">>>>>>>>><<<<<<<<<<")
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print(">>>>>>>>><<<<<<<<<<")
        print("Boss won!!!")
        print(">>>>>>>>><<<<<<<<<<<")
    return all_heroes_dead


def round(boss, heroes):
    global round_number
    round_number += 1
    boss.hit(boss, heroes)
    for hero in heroes:
        hero.hit(boss)
        hero.apply_super_ability(boss, heroes)
    print_statistics(boss, heroes)


def start():
    boss = Boss("OverLord", randint(700, 2000), 50)
    magic = Magic("Samuel", randint(250, 300), 20)
    berserk = Berserk("Darkness", randint(250, 320), 30)
    golem = Golem("Oleg", randint(500, 800), 2)
    witcher = Witcher("Chaser", randint(400, 500), 0)
    hacker = Hacker("Alex", randint(220, 300), 20)


    heroes = [magic,berserk ,golem, witcher, hacker]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        round(boss, heroes)


start()
