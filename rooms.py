import random
import time
import math
import source as sgs
import combat as combat
import tags as tags

#type can be "c" combat, "l" level, "s" skill, "h" heal, "g" growth, "b" boss, "e" elite

class room:
    def __init__(self, name, type, diff):
        self.name=name
        self.type=type
        self.diff=diff
        self.occ=None
        if self.type == "c":
            pass
        elif self.type == "e":
            pass
        elif self.type =="b":
            pass
    def display(self):
        pass

    def enter(self, player):
        if self.type == "c" or self.type =="b":
            return encounter(player, self.occ)

class floor:
    def __init__(self, rooms):
        self.rooms=rooms

    def enter(self,player,room_n):
        if ((self.rooms[room_n].enter())==True):
            return True
        else:
            return False

    def display(self):
        pass


def generate_floor(room_number):
    pass

def generate_enemy(room_number, type):
    pass
