import random
import time
import source as sgs
import combat as combat
import rooms as rooms

#just a file for testing

#testing lines
#placeholder skills
A1=sgs.skill("Attack", 1, 0, "PHY")
A8=sgs.skill("Decimate", 8, "Cripple", "PHY")
M1=sgs.skill("Cast", 1, "Drain" , "MAG")
M5=sgs.skill("Burst", 5, "Broken", "MAG")
S1=sgs.skill("Analyze A", 0, "Scan" , "MAG")
S3=sgs.skill("Analyze B", 1.5, "Scan" , "MAG")

#default character
p1 = sgs.character("PLAYER",10,3,3,3,3)
p1.add_skill(A1,"n")
p1.add_skill(A8,"n")
p1.add_skill(S1,"n")
p1.add_skill(S3,"n")
p1.add_skill(M1,"n")
p1.add_skill(M5,"n")

#default enemy
e1 = sgs.character("ENEMY",10,3,4,2,3)

action=0

print("!!! only intended for testing purposes, does not sanitize all inputs")

while(action!=9):
    try:
        action=int(input("testing(add level(1), encounter(2), loottest(3), status(4), add growths(5), encounter room(6), exit(9)):"))
        print()
    except ValueError:
        print("not valid input")
        print()
    if action == 1:
        level = int(input("+level:"))
        print()
        print("Gains: "+ str(p1.level_up(level)))
        p1.display_all()
    elif action == 2:
        print("combat test:")
        print()
        e1 = sgs.character("ENEMY",10,3,4,2,3)
        e1.level_up(int(p1.level)-1)
        e1.add_skill(A1,"n")
        e1.add_skill(A8,"n")
        e1.add_skill(M1,"n")
        e1.add_skill(M1,"n")
        e1.add_skill(M1,"n")
        e1.add_skill(M5,"n")
        e1.add_loot(A8)
        success = combat.encounter(p1,e1)
        if success == (True):
            print("Finished!")
        else:
            print("Finished!")
    elif action == 3:
        e1.add_loot(A8)
        e1.display_loot()
        print("WAITING...")
        time.sleep(3)
        e1.drop_loot(p1)
    elif action == 4:
        p1.display_all()
        e1.display_all()
    elif action == 5:
        stats=["hp","atk","def","mag","agl"]
        growth=[]
        for i in range(0,5):
            ele = int(input(stats[i]+": "))
            growth.append(ele)
        p1.add_growths(growth)
        for i in range(0,5):
            print(stats[i] + ": " + str(p1.weights[i]) + "%")
    elif action == 6:
      r1=rooms.room("c",p1.level)
      r1.display()
      r1.enter(p1) 