from util import type_out
import random

#Player Class 

# ENCAPSULATION (health via @property)
# STATE TRACKING (inventory, potion effects)
# CONDITIONAL LOGIC (for using/discarding items)

class Player:
    def __init__(self, name, element, max_health=100): #Basic Player Setup
        self.name = name
        self.element = element
        self._health = max_health #protected variable
        self.max_health = max_health
        self.inventory = [] 
        self.weakening_potion_active = False
        self.max_inventory = 2

    # Encapsulation of Health 

    @property #decorator
    def health(self):
        return self._health
    
    # ENCAPSULATION: manage health through methods, not direct access

    def take_damage(self, amount): #reduces player's health when taking damage
        self._health -= amount
        if self._health < 0:
            self._health = 0
        type_out(f"You took {amount} damage! Current health: {self._health}/{self.max_health}")

    def heal(self, amount): #increases player's health if healing potion used
        old = self._health
        self._health += amount
        if self._health > self.max_health:
            self._health = self.max_health
        type_out(f"You healed {self._health - old} HP. Health: {self._health}/{self.max_health}")

    def is_alive(self): #check if player is alive
        return self._health > 0


    def add_item(self, item): #add items to inventory
        if len(self.inventory) >= self.max_inventory:
            type_out("\nYour inventory is full (max 2 items).")
            self.manage_full_inventory(item)
        else:
            self.inventory.append(item)
            type_out(f"You picked up a {item}!")

    def manage_full_inventory(self, new_item): #manages inventory when full
        type_out(f"Inventory: {self.inventory}")
        choice = input(f"Do you want to use or discard an existing item to pick up '{new_item}'? (use/discard/skip): ").lower()
        if choice == "use":
            self.use_potion_from_inventory()
            if len(self.inventory) < self.max_inventory:
                self.inventory.append(new_item)
                type_out(f"You picked up a {new_item}.")
        elif choice == "discard":
            self.discard_item()
            if len(self.inventory) < self.max_inventory:
                self.inventory.append(new_item)
                type_out(f"You picked up a {new_item}.")
        else:
            type_out("You decided not to pick up the new item.")

    def discard_item(self): #discards an item from inventory
        if not self.inventory:
            type_out("Your inventory is empty.")
            return
        type_out("\nSelect an item to discard:")
        for i, item in enumerate(self.inventory, 1):
            type_out(f"{i}. {item}")
        try:
            index = int(input("Enter the number of the item to discard: ")) - 1
            if 0 <= index < len(self.inventory):
                removed = self.inventory.pop(index)
                type_out(f"You discarded {removed}.")
            else:
                type_out("Invalid selection.")
        except ValueError:
            type_out("Invalid input.")

    def use_potion_from_inventory(self): #uses potion from inventory
        if not self.inventory:
            type_out("Your inventory is empty.")
            return
        type_out("\nSelect a potion to use:")
        for i, item in enumerate(self.inventory, 1):
            type_out(f"{i}. {item}")
        try:
            index = int(input("Enter the number of the potion to use: ")) - 1
            if 0 <= index < len(self.inventory):
                potion = self.inventory.pop(index)
                if potion == "Healing Potion":
                    self.heal(30)
                elif potion == "Weakening Potion":
                    type_out("You used a Weakening Potion. The next enemy will be weaker.")
                    self.weakening_potion_active = True
            else:
                type_out("Invalid selection.")
        except ValueError:
            type_out("Invalid input.")

    def use_potion_before_battle(self): #option to use a potion before a battle begins
        if not self.inventory:
            type_out("You have no potions to use.")
            return
        type_out(f"\nInventory: {self.inventory}")
        choice = input("Use a potion before battle? (healing/weakening/none): ").strip().lower()
        if choice == "healing" and "Healing Potion" in self.inventory:
            self.inventory.remove("Healing Potion")
            self.heal(30)
        elif choice == "weakening" and "Weakening Potion" in self.inventory:
            self.weakening_potion_active = True
            self.inventory.remove("Weakening Potion")
            type_out("You used a Weakening Potion. The next enemy will be weaker.")
        elif choice == "none":
            type_out("You choose not to use any potion.")
        else:
            type_out("Invalid choice or potion not available.")

    def choose_battle_reward(self): #choose a reward after battle has been won
        type_out("\nChoose your reward:")
        type_out("1. Healing Potion")
        type_out("2. Weakening Potion")
        choice = input("Pick 1 or 2: ").strip()
        if choice == "1":
            self.add_item("Healing Potion")
        elif choice == "2":
            self.add_item("Weakening Potion")
        else:
            type_out("Invalid choice — no reward added.")

