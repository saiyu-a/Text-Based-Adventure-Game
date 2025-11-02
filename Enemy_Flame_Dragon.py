import time
from util import type_out
from Enemy_Parent import Enemy

class FlameDragon(Enemy):
    def __init__(self, base_difficulty=1.3):
        super().__init__("Flame Dragon", "Fire", base_difficulty)

    def attack(self, player): #battle code
        type_out("\nThe sky glows crimson as the Flame Dragon descends, its wings crackling with fire...")
        type_out("\nTo defeat the dragon, you have to type 'extinguish' 3 times in 10 seconds to extinguish its flames.")
        target_word = "extinguish"
        repeats = 3
        if player.weakening_potion_active: #checks if weakening potion used
            type_out("Your weakening potion swirls into the smoke, dimming the Dragon's flames and reducing its fury.")
            type_out("You now only have to type 'extinguish' 2 times")
            repeats = 2 
            player.weakening_potion_active = False
        type_out("The Flame Dragon roars: 'Prove your swiftness, mortal!'")
        input("Press Enter to start typing...")
        start = time.time()
        for i in range(repeats):
            attempt = input(f"{i+1}/{repeats}: ").strip().lower()
            if attempt != target_word:
                damage = self.calculate_damage(12, self.base_difficulty)
                player.take_damage(damage)
                if not player.is_alive():
                    return "lose"
                else:
                    return "fail"
        elapsed = time.time() - start
        if elapsed <= 10:
            type_out("You defeated the Flame Dragon!")
            self.mark_defeated()
            return "win"
        else:
            damage = self.calculate_damage(12, self.base_difficulty)
            player.take_damage(damage)
            return "lose" if not player.is_alive() else "fail"