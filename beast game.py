import random
import time
import math

from colorama import init
from termcolor import colored

init()


start = "y"

class Fighter:

    def __init__(self, hp):
        self.attack = 0
        self.hp = hp
    def is_dead(self):
        return self.hp <= 0
    def power_talk(self):
        if self.attack >= 40:
            print(colored("WOW! It was super powerful!","yellow",'on_black', ['bold']))
        elif self.attack <= 10:
            print(colored("It was not so powerful...","blue"))

class Attack:

    def __init__(self, name, chance, get_damage, range, uses):
        self.name = name
        self.chance = chance
        self.get_damage = get_damage
        self.range = range
        self.uses = uses

while start == "y":

    user = Fighter(250)
    beast = Fighter(random.randint(50,350))
     
    attacks = [
    Attack("Punch",9,lambda: random.randint(5,15),"5-15",math.inf),
    Attack("Spell",3,lambda: random.randint(25,50),"25-50",5),
    Attack("Gunshot",1,lambda: random.randint(99,100),"99-100",2),
    Attack("Kick",7,lambda: random.randint(10,25),"10-25",10)
]

    print("There is a scary beast. and he want to fight.... oh no")
    time.sleep(1)
    print("You must battle the beast! and save your country!!!!!!")
    time.sleep(1)
    print(f"You begin with {user.hp} HP and the beast has {beast.hp} HP")

    while True:
        print()
        user_move = input("Attack or defend?: ")
        
        beast.attack = random.randint(1,25)

        if user_move == "attack" or user_move == "a":

            while True:
                attack_type = input("Pick an attack! Type in a number for an attack, or press '?' to list the attacks: ")
                
                if attack_type == "?":
                    for index, attack in enumerate(attacks):
                        print(f"[{index}]: {attack.name} can deal {attack.range} damage points, be used {attack.uses} times, and has a {attack.chance} out of 10 chance of working.")
                    continue

                try:
                    chosen_attack = attacks[int(attack_type)]
                except IndexError:
                    continue

                if chosen_attack.uses == 0:
                    print("You're out of uses! Choose a different attack. Press '?' to check your uses on each attack.")
                    continue
                break


            chance_attack = random.randint(1,10)
            chosen_attack.uses = chosen_attack.uses - 1

            if chance_attack < chosen_attack.chance:

                user.attack = chosen_attack.get_damage()

                print(colored("You dealt " + str(user.attack) + " damage to the beast!","green"))

                beast.hp = beast.hp - user.attack
                user.power_talk()

                if beast.is_dead():
                    print("YOU WON!!!!!!!!")
                    time.sleep(2)
                    start = input("Replay (y/n)?: ")
                    break
            else:
                print(colored(f"Your {chosen_attack.name} failed!", "red"))

        elif user_move == "defend" or user_move == "d":
            defend = random.randint(1,3)
            if defend == 1:
                print(colored("Your defenses weren't enough! The beast still attacked you!","red"))

            else:

                print(colored("You prevailed against the beast!","green"))
                time.sleep(1)
                beast.attack = 0
                print("No HP lost")
                time.sleep(1)

                rock_chance = random.randint(1,4)
                if rock_chance == 1:
                    rock_damage = random.randint(25,50)
                    beast.hp = beast.hp - rock_damage
                    
                    print(colored(f"The beast tripped over a rock and seriously hurt itself! It lost {rock_damage} HP", "green"))


        else: 
            continue

        user.hp = user.hp - beast.attack
        
        if beast.attack > 0:
            print("The beast attacks you!")
            time.sleep(1)
            print(colored("The beast did " + str(beast.attack) + " damage to you!", "red"))
            beast.power_talk()
            if user.is_dead():
                print("The beast won...")
                time.sleep(2)
                start = input("Replay (y/n)?: ")
                break
        
        print("The beast now has " + str(beast.hp) + " HP left")
        time.sleep(1)
        print("And you have " + str(user.hp) + " HP left!")
