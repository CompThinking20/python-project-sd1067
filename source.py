import random
import time
import math

class Error(Exception):
    pass
class NoSkillError(Error): #might be unnecessary
    pass
class NaNError(Error): #for scrubbing inputs
    pass

class character:
    def __init__(self, name, mhp, atk, df, mag, agl):
        self.name=name
        self.mhp=mhp #maximum hp, hp should never go over
        self.hp=mhp #when character is created, sets hp to max
        self.atk=atk #used in phy attcks
        self.df=df #used to reduce Phy damage
        self.mag=mag #used to deal and block mag damage
        self.agl=agl #detemines turn order
        self.level=1
        self.skills=[] #list of skills to be accessed later
        self.status="Normal"
        #chance in % to gain respective stat upon leveling
        self.weights=[10,10,10,10,10]
        self.drops=[]
    #for display purposes
    def display_title(self):#displays name and level
        print(str(self.name) + " Lv " + str(self.level))
    def display_status(self):#displays name, level, status, and stats
        print(str(self.name) + " Lv " + str(self.level) +"  "+ str(self.hp) + "/" + str(self.mhp) +  " HP | " + str(self.status))
        print("Atk:" + str(self.get_atk()) + " / Def:" + str(self.get_df()) + " / Mag:" + str(self.get_mag()) + " / Agl:" + str(self.get_agl()))
    def display_actions(self):#displays all actions this character can take
        print("[]-----------------------------------------------[]")
        print("Skills:")
        count=0
        for x in self.skills: #iterates and prints skills
            print()
            print("-[" + str(count) + "]-: " + str(x.name))
            x.display()
            count=count+1
        print("[]-----------------------------------------------[]")
    def display_loot(self):#displays what this character will drop
        print("[]-----------------------------------------------[]")
        print("Loot:")
        for x in range(len(self.drops)):
            if x == 0:
                print("+ LEVEL UP")
            else:
                print("+ [DROP] " + self.drops[x].name)
                self.drops[x].display()
        print("[]-----------------------------------------------[]")
    #display everything relevant in a character
    def display_all(self):
        self.display_status()
        self.display_actions()
        if len(self.drops)!=0:
            self.display_loot()
    #change growth rates
    def add_growths(self, growths):
        for x in range(5):
            self.weights[x] = self.weights[x] + int(growths[x])
    #adds skills and prompts if user wants to replace one
    def add_skill(self, skl, disp):
        decide=""
        sk2rpl=0
        if len(self.skills) > 5:
            while(True):#all of the try-catch bocks are pretty much just scrubbing inputs
                try:
                    decide = str(input("(y/n) Replace a skill with " + str(skl.name) + "?"))
                    if (decide == "y" or decide == "n") == False:
                        raise NaNError
                    break
                except NaNError:
                    print("Not a valid input. Please try again.")
                    print()
            if decide == "y":
                while(True):
                    try:
                        print("Replace with:")
                        print("-[]-:" + str(skl.name))
                        skl.display()
                        self.display_actions()
                        sk2rpl = int(input("Select Skill to Replace:"))
                        if (0<=sk2rpl<=5)==False:
                            raise NaNError
                        break
                    except TypeError:
                        print("Not a valid input. Please try again.")
                        print()
                    except ValueError:
                        print("Not a valid input. Please try again.")
                        print()
                    except NaNError:
                        print("Not a valid input. Please try again.")
                        print()
                self.skills[sk2rpl] = skl
                print("Replacement Complete!")
            elif decide == "n":
                print(str(skl.name) + " discarded.")
            print()
        else:
            self.skills.append(skl)
            decide="y"
            if str(disp)==decide:
                print(str(skl.name) + " added to " + str(self.name)+"'s skills!")
                print()
    #add drops and dropping upon victory
    def add_loot(self, drop):
        if len(self.drops)==0:
            self.drops.append(1)
        self.drops.append(drop)
        if len(self.drops) > 4:
            self.drops.remove(self.drops[1])
    def drop_loot(self, victor):#drops loot
        stat=["MHP","ATK","DF","MAG","AGL"]
        for x in range(int(len(self.drops))):
            if x == 0:
                print("-+-+- LEVEL UP! -+-+-")
                print("Level: " + str(victor.level) + (" >>> ") + str(victor.level+1))
                d=victor.level_up(1)
                for y in range(5):
                    print("+" + str(d[y]) + " " + str(stat[y]))
            if x >= 1:
                print("DROP: " + str(self.drops[x].name))
                self.drops[x].display()
                victor.add_skill(self.drops[x],"y")
        self.drops=[]#clears loot
    #makes healing easy
    def heal(self, heal_amt):
        self.hp = int(self.hp) + int(heal_amt)
        if int(self.hp)  > int(self.mhp):
            self.hp = int(self.mhp)
        print(str(self.name) + " healed to " + str(self.hp ) + "/" + str(self.mhp) + "HP (" + str(heal_amt) + " healed)")
    #level up function, returns the amount each stat leveled up by
    def level_up(self, amt):
        self.level = int(self.level) + int(amt)
        random.seed(None,2)
        results=[0,0,0,0,0]
        for x in range(amt):
            for y in range(5):
                if (random.randint(0,100)) <= ((int(self.weights[y]))%100):
                    success=1
                else:
                    success=0
                results[y] += int((int(self.weights[y])/100)+success)
        self.mhp = int(self.mhp) + int(results[0])
        self.hp = int(self.hp) + int(results[0])
        self.atk = int(self.atk) + int(results[1])
        self.df = int(self.df) + int(results[2])
        self.mag = int(self.mag) + int(results[3])
        self.agl = int(self.agl) + int(results[4])
        return results
    #use in encounter function(might be redundant)
    def b_action(self, action, target):
        self.skills[action].apply(self, target)
    #calculates each stat with statuses applied
    def get_atk(self):
        if self.status == "Crippled" or self.status == "Weakened":
            ratk = int(self.atk/2)
            return ratk
        else:
            return self.atk
    def get_df(self):
        if self.status == "Opened" or self.status == "Broken":
            rdf = int(self.df/2)
            return rdf
        else:
            return self.df
    def get_mag(self):
        if self.status == "Broken" or self.status == "Weakened":
            rmag = int(self.mag/2)
            return rmag
        else:
            return self.mag
    def get_agl(self):
        if self.status == "Crippled" or self.status == "Opened":
            ragl = int(self.agl/2)
            return ragl
        else:
            return self.agl

class skill:#skills for use 
    def __init__(self, name, damage, effect, dtype):
        self.name=name
        self.damage=damage
        self.effect=effect
        self.dtype=dtype #name/damage multiplier/status effect/damage type
    def display(self): #display function for ease of use
        print("->>Potency: " + str(self.damage) + "x / Type: "+ str(self.dtype))
        if self.effect != 0:
            print("->>Effect: Inflicts " + str(self.effect))
    def apply(self, caster, target): #actually using the skill, uses stats of the caster vs defenses of target
        print()
        damage_done=0
        #Changing the damage done based on type of the skill
        if self.dtype == "MAG":
            damage_done = int((self.damage * int(caster.get_mag())) - int(target.get_mag()))
        elif self.dtype == "PHY":
            damage_done = int((self.damage * int(caster.get_atk())) - int(target.get_df()))
        if damage_done <= 0 and self.damage > 0:
            damage_done = 1 #Minimal damage is 1

        target.hp = target.hp - damage_done #damage goes through

        if self.damage > 0: #display damage
            time.sleep(1)
            print(str(caster.name) + "'s " + str(self.name) + " did " + str(damage_done) + " damage to " + str(target.name)+"!")
            print(str(target.name)+" has " + str(target.hp) + "/" + str(target.mhp) + " HP left!")
        if self.effect != 0 and self.effect != "Drain" and self.effect != "Scan" : #display effects and apply them, only if they are applicable
            time.sleep(1)
            target.status = self.effect
            print(str(target.name) + " was inflicted with " + str(self.effect) + "!")
        elif self.effect == "Drain": #Apply heal equal to halp of damage dealt
            time.sleep(1)
            heal = int(damage_done/2)
            caster.heal(heal)
        elif self.effect == "Scan":#allows player to see the ability the enemy has 
            time.sleep(1)
            print("0000000000000000000000000000000")
            print("Scanned "+str(target.name)+":")
            print("0000000000000000000000000000000")
            target.display_actions()
            target.display_loot()
            input("o0o0o Awaiting Input to Move on o0o0o")
        time.sleep(1)
        print()
