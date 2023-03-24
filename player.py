"""

"""
import tkinter as tk
import tkinter.font as tkFont

class Character:
    def __init__(self, health, attack, defense, speed):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed



class Player(Character):
    def __init__(self, health, attack, defense, speed, inventory):
        super().__init__(health, attack, defense, speed)
        self.inventory = inventory

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def get_inventory(self):
        return self.inventory

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

    def set_health(self, health):
        self.health = health

    def set_attack(self, attack):
        self.attack = attack

    def set_defense(self, defense):
        self.defense = defense

    def set_speed(self, speed):
        self.speed = speed

    def __str__(self):
        return f"Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}"

class Enemy(Character):
    def __init__(self, health, attack, defense, speed, name):
        super().__init__(health, attack, defense, speed)
        self.name = name

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

    def set_health(self, health):
        self.health = health

    def set_attack(self, attack):
        self.attack = attack

    def set_defense(self, defense):
        self.defense = defense

    def set_speed(self, speed):
        self.speed = speed

    def __str__(self):
        return f"Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}"

class Item(object):
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_value(self):
        return self.value

    def __str__(self):
        return f"{self.name}: {self.description}. Value: {self.value}"


