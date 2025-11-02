from util import type_out

#Base Class for ALL Enemies

# INHERITANCE (used by all enemies)
# ENCAPSULATION (private attribute for defeated state)

class Enemy:
    total_defeated = 0  #counter of total defeated enemies   # CLASS ATTRIBUTE shared by all enemies

    def __init__(self, name, element, base_difficulty): 
        self.name = name
        self.element = element
        self.base_difficulty = base_difficulty
        self.__defeated = False  #private variable - to track if enemy is defeated - ENCAPSULATED attribute

    def is_defeated(self):  
        return self.__defeated #returns TRUE if enemy is defeated

    # Abstract-style method overridden by subclasses (POLYMORPHISM)
    
    def attack(self, player):
        pass

    def calculate_damage(self, base, difficulty_modifier): #calculate damage based on difficulty
        return int(base * difficulty_modifier)

    def mark_defeated(self): #marks enemy as DEFEATED
        self.__defeated = True
        Enemy.total_defeated += 1

    def __str__(self): #returns enemy status as text
        status = "Defeated" if self.__defeated else "Ready to battle" 
        return f"{self.name} ({self.element}) - Difficulty: {self.base_difficulty} | {status}"