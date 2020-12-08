import random
import time
import math
import source as sgs
import combat as combat
import tags as tags

#type can be "c" combat, "h" heal, "g" growth, "b" boss, "e" elite
#all currenty wip

class room: #rooms to enter
    def __init__(self, type, diff):
        self.type=type
        self.diff=diff
        self.occ=None
        #generate enemy of scaling difficulty
        if self.type == "c":
            self.occ=generate_enemy(diff)
        elif self.type == "e":
            self.occ=generate_enemy(diff+3)
        elif self.type =="b":
            self.occ=generate_enemy(diff+5)

    def display(self):#hints as to whats behind the door before entering
        if self.type=="h":
          print("A green door. It feels calm...")
        elif self.type=="g":
          print("A blue door. It feels calm...")
        elif self.type=="c":
          print("A red door. You feel a presence behind it...")
        elif self.type=="e":
          print("A red door. You feel a disturbing presence behind it...")
        elif self.type=="b":
          print("A red door. You feel a threatening presence behind it!!!")

    def enter(self, player):#starts encounter with occupant or heals or adds growths
        if self.type == "c" or self.type =="b" or self.type=="e":
            return combat.encounter(player, self.occ)
        elif self.type == "h":
          print("You enter the fountain of healing.")
          player.heal(9999)
          player.status="Normal"
          time.sleep(1)
          print("You feel the pain wash away...")
          input("+-+-+ Awaiting Input to Move on +-+-+")
          return True
        elif self.type=="g":
          player.add_growths([20,20,20,20,20])
          print("You feel your potential grow...")
          input("+-+-+ Awaiting Input to Move on +-+-+")
          return True

def generate_skill(level):#generates a random skill 
  s=None
  random.seed()
  stag1=0
  stag2=0
  sbase=random.choice(["Slash","Cast","Burst","Bash"])
  #scaling damage base on level
  if level < 10:
    damage=random.choice(["Miniscule ","Small ","Medium "])
  elif level < 20:
    damage=random.choice(["Miniscule ","Small ","Medium ","Huge ","Immense "])
  elif level >= 20:
    damage = random.choice(["Medium ","Huge ","Immense ","Collossal "]) 
  #adds tags the higher level it is
  if level < 10 and damage != "Medium ":
    stag1=random.choice(["Vampiric ","Libra","Maiming ","Exposing ","Pressure ","Crushing "])
  elif level < 20 and damage != "Immense ":
    stag1=random.choice(["Vampiric ","Libra","Maiming ","Exposing ","Pressure ","Crushing "])
  elif level < 30:
    stag1=random.choice(["Vampiric ","Libra","Maiming ","Exposing ","Pressure ","Crushing "])
    stag2=random.choice(["Cursed ", "Enhanced "])
  elif level >= 30:
    stag1=random.choice(["Vampiric ","Libra","Maiming ","Exposing ","Pressure ","Crushing "])
    stag2=random.choice(["God-Blessed ","Cursed ", "Enhanced "])
  #setting a name
  if stag1 == 0 and stag2 == 0:
    name=damage+sbase
  elif stag2 == 0:
    name=damage+stag1+sbase
  else:
    name=stag2+damage+stag1+sbase
  #Creating the skill using all of our random information
  if stag2==0:
    s=sgs.skill(name,tags.skill_damage[damage],tags.skill_secondary[stag1],tags.skill_primary[sbase])
  else:
    s=sgs.skill(name,tags.skill_damage[damage]+tags.skill_tag[stag2],tags.skill_secondary[stag1],tags.skill_primary[sbase])
  return s

def generate_enemy(level):
  e=None
  random.seed()
  #randomly sets stuff
  base=random.choice(["Titan","Cultist","Goblin","Crawler","Wraith","Spider"])
  tag1=random.choice(["Fire God's ","Thunder God's ","Water God's ","Wind God's ","Nature God's "])
  tag2=random.choice(["Giant ","Enraged ","Shining ","Enchanted ","Berserk ","Extreme ","Agile ","Protected "])
  #tags are only added if the level meets the requirement
  if level < 10:
    e = sgs.character(base,3,3,3,3,3)
    e.add_growths(tags.enemy_classes[base])
  elif level < 20:
    name=tag2+base
    e = sgs.character(name,5,5,5,5,5)
    e.add_growths(tags.enemy_classes[base])
    e.add_growths(tags.enemy_tags[tag2])
  elif level >= 20:
    name=tag1+tag2+base
    e = sgs.character(name,5,5,5,5,5)
    e.add_growths(tags.enemy_classes[base])
    e.add_growths(tags.enemy_tags[tag2])
    e.add_growths(tags.enemy_names[tag1])
  #generating skills for enemy to use
  skill1=generate_skill(level)
  skill2=generate_skill(level)
  skill3=generate_skill(level)
  e.add_skill(skill1,"n")
  e.add_skill(skill2,"n")
  e.add_skill(skill3,"n")
  #adds the first skill as loot
  e.add_loot(skill1)
  #adds skill and loot if the level is high enough
  if level >= 40:
    skill4=generate_skill(level)
    e.add_skill(skill4,"n")
    e.add_loot(skill4)
  #adding levels to match difficulty
  e.level_up(level-1)
  return e




