import tkinter as tk
import tkinter.font as tkFont

class Player:
    def __init__(self, health, inventory, armor):
        self.health = health
        self.inventory = inventory
        self.armor = armor





class inventory(Player):
    def __init__(self, item, health, inventory, armor):
        super().__init__(health=100, inventory={}, armor=0)
        self.item = item

