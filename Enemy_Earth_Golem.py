import random
from util import type_out
from Enemy_Parent import Enemy

class EarthGolem(Enemy):
    def __init__(self, base_difficulty=1.0):
        super().__init__("Earth Golem", "Earth", base_difficulty)

    def attack(self, player): #battle code
        type_out("\nThe ground trembles as the Earth Golem awakens from its slumber...")
        type_out("You must defeat the Golem in a game of Rock, Paper, Scissors.")
        choices = ["rock", "paper", "scissors"]
        golem_choice = random.choice(choices)

        # AGGREGATION: Enemy uses the player object but doesn't own it

        if player.weakening_potion_active:
            type_out("Your weakening potion lets you sense the Golem's move...")
            unavailable = random.choice(choices)
            type_out(f"The Golem will NOT choose {unavailable.upper()}.")
            choices = [c for c in choices if c != unavailable]
            golem_choice = random.choice(choices)
            player.weakening_potion_active = False
        type_out("The Earth Golem rumbles: 'Show me your strength, human!'")
        while True:
            player_choice = input("Choose rock, paper, or scissors: ").lower()
            if player_choice not in ["rock", "paper", "scissors"]:
                type_out("Invalid choice.")
                continue 
            type_out(f"The Golem chose {golem_choice.upper()}!")
            if player_choice == golem_choice:
                type_out("It's a draw! Try again.")
                golem_choice = random.choice(choices)
                continue
            elif (player_choice == "rock" and golem_choice == "scissors") or \
                 (player_choice == "paper" and golem_choice == "rock") or \
                 (player_choice == "scissors" and golem_choice == "paper"):
                type_out("You smashed the Golem's defense!")
                self.mark_defeated()
                return "win"
            else:
                damage = self.calculate_damage(10, self.base_difficulty)
                player.take_damage(damage)
                if not player.is_alive():
                    return "lose"