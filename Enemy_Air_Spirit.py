import random
import time
import os
from util import type_out
from Enemy_Parent import Enemy

class AirSpirit(Enemy):
    def __init__(self, base_difficulty=1.5):
        super().__init__("Air Spirit", "Air", base_difficulty)
        self.words = ["wind", "cloud", "breeze", "sky", "feather", "whisper", "storm", "flight"]

    def attack(self, player):
        type_out("\nThe air grows cold and still. The Air Spirit materializes from a swirl of mist...")
        type_out("The Air Spirit's voice echoes: 'Prove your focus, mortal. The winds test your memory!'")
        type_out("To defeat the spirit, you must correctly recall the words it whispers before they vanish into the air.")
        length = 4
        if player.weakening_potion_active:
            type_out("Your potion spreads through the air, calming the chaotic winds. The test will be slightly easier.")
            length = 3
            player.weakening_potion_active = False
        sequence = random.sample(self.words, length)
        type_out("Memorize this sequence:")
        type_out(" ".join(sequence))
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')  
        answer = input("Type the sequence back (space-separated): ").strip().lower().split()
        if answer == sequence:
            type_out("You perfectly recall the whispers of the wind! The Air Spirit bows to your mind.")
            self.mark_defeated()
            return "win"
        else:
            damage = self.calculate_damage(14, self.base_difficulty)
            type_out(f"Incorrect! The winds lash at you for {damage} damage.")
            player.take_damage(damage)
            if not player.is_alive():
                return "lose"