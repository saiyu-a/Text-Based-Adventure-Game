import random
from util import type_out
from Enemy_Parent import Enemy

class WaterSerpent(Enemy):
    def __init__(self, base_difficulty=1.2): #riddle battle logic
        super().__init__("Water Serpent", "Water", base_difficulty)
        self.riddles = [
            {"question": "I am tall when I am young and short when I am old. What am I?", "answer": "candle", "hint": "I melt away as I give you light."},
            {"question": "What has to be broken before you can use it?", "answer": "egg", "hint": "You find me in the kitchen, fragile and white."},
            {"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps", "hint": "You leave me behind as you move forward."},
            {"question": "What has keys but cannot open locks?", "answer": "piano", "hint": "I create melodies, not unlocked doors."},
            {"question": "What gets wetter the more it dries?", "answer": "towel", "hint": "I dry others but become soaked myself."}
        ]

    def attack(self, player): #battle code
        type_out("\nA ripple disturbs the calm waters as the Water Serpent rises from the depths...")
        if player.weakening_potion_active: #checks if weakening potion used
            type_out("The potion's power seeps into the waves, slowing the serpent's coils. Its mind fogs slightly — you sense a hint will be whispered to you.")
        type_out("The Water Serpent hisses: 'Answer my riddle to pass!'")

        riddle = random.choice(self.riddles) 
        print(f"\nRiddle: {riddle['question']}")
        if player.weakening_potion_active: #gives hint if weakening potion used
            print(f"(Hint: {riddle['hint']})")
            player.weakening_potion_active = False

        answer = input("Your answer: ").strip().lower()
        if answer == riddle["answer"]:
            print("Correct! You defeated the Water Serpent!")
            self.mark_defeated()
            return "win"
        else:
            damage = self.calculate_damage(10, self.base_difficulty)
            print(f"Wrong! The serpent strikes for {damage} damage.")
            player.take_damage(damage)
            if not player.is_alive():
                return "lose"