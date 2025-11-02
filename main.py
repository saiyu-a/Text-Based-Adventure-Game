import sys
from util import type_out
from Player import Player
from Enemy_Earth_Golem import EarthGolem
from Enemy_Water_Serpent import WaterSerpent
from Enemy_Flame_Dragon import FlameDragon
from Enemy_Air_Spirit import AirSpirit
from Enemy_Parent import Enemy

def choose_next_enemy(enemies): #lets player choose next enemy to fight
    available = [e for e in enemies if not e.is_defeated()]
    if not available:
        return None
    type_out("\nChoose your next enemy:")
    for i, e in enumerate(available, 1):
        type_out(f"{i}. {e.name}")
    while True:
        try:
            choice = int(input("Enter number: "))
            return available[choice - 1]
        except (ValueError, IndexError):
            type_out("Invalid choice.")

def scale_difficulties(enemies, warrior): #adjusts realm's difficulty based on player's element
    order_map = {
        "Fire":  ["Fire", "Earth", "Air", "Water"],
        "Earth": ["Earth", "Air", "Water", "Fire"],
        "Air":   ["Air", "Water", "Fire", "Earth"],
        "Water": ["Water", "Fire", "Earth", "Air"]
    }
    multipliers = [0.8, 1.0, 1.2, 1.4]  
    order = order_map.get(warrior, ["Earth", "Water", "Fire", "Air"])
    for e in enemies:
        if e.element in order:
            idx = order.index(e.element)
            e.base_difficulty *= multipliers[idx]

if __name__ == "__main__":
    #intro story text
    type_out(f'Welcome, traveler... \nThe balance of the elemental realms has been shattered. \nFour ancient spirits — Earth, Fire, Water, and Air — have risen once more, each guarding their domain with untamed power. \nOnly a true warrior, one who understands both strength and wisdom, can restore harmony to the worlds. \nYou are that warrior. \nRestore balance. Defeat the spirits. Prove yourself worthy of the elements.')
    #Player set up
    name = input("Enter your name: ")
    element = input("What kind of warrior would you like to be? (Earth/Water/Fire/Air): ").capitalize()
    if element not in ["Earth", "Water", "Fire", "Air"]: #default to Earth if input is invalid
        print("Invalid choice. Defaulting to Earth.")       
        element = "Earth"
    type_out(f'Welcome {name} the {element} Warrior! You shall start your journey in your homeland: {element} Realm')
    player = Player(name, element)

    earth = EarthGolem()
    water = WaterSerpent()
    fire = FlameDragon()
    air = AirSpirit()
    enemies = [earth, water, fire, air]
    element_map = {"Earth": earth, "Water": water, "Fire": fire, "Air": air}
    
    scale_difficulties(enemies, element)

    #handle first battle outcome

    first_enemy = element_map[element]
    type_out(f"\nYour first battle will be in the {element} Realm against the {first_enemy.name}!")
    player.use_potion_before_battle()
    result = first_enemy.attack(player)
    if result == "win":
         if Enemy.total_defeated < 4:  
            player.choose_battle_reward()
    elif result == "lose":
        type_out("You have fallen in battle.")
        exit()
    
    #loop for next battles

    while player.is_alive() and any(not e.is_defeated() for e in enemies):
        next_enemy = choose_next_enemy(enemies)
        if not next_enemy:
            break
        player.use_potion_before_battle()
        result = next_enemy.attack(player)
        if result == "win":
            if Enemy.total_defeated < 4:  
                player.choose_battle_reward()
        elif result == "lose":
            type_out("You have fallen in battle.")
            break

    #Ending message  

    if player.is_alive():
        type_out("\nCongratulations! You restored balance to all four realms!")
    else:
        type_out("\nGame Over.")
