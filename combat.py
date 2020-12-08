import random
import time

def encounter( player , enemy ): #combat function
    ptimer=1000
    etimer=1000
    print("____________________________________") #aesthetic purposes
    print()
    player.display_title()
    print("VS")
    enemy.display_title()
    print("____________________________________")
    print()
    input("o0o0o Awaiting Input to Start Combat o0o0o")
    #intended turn design: higher agl allows a character to go faster
    #two 'timers' run concurrently, one for each combatant
    #every cycle, the character's agl is subtracted from the timer until
    #one reaches zero or lower, at which point someone takes a turn
    while int(player.hp) > 0 and int(enemy.hp) > 0: #tracks whether one reaches 0 hp first
        paction=0 #setting this var early
        while ptimer > 0 and etimer > 0:
            ptimer= ptimer - int(player.get_agl())
            etimer= etimer - int(enemy.get_agl())
        if ptimer <= 0 and etimer <= 0: #accounting for a when timers reach 0 at the same time, the higher agl gets prioritized
            if int(enemy.get_agl()) > int(player.get_agl()):
                ptimer = 1
            else:
                etimer = 1
        if ptimer <= 0:#Allows User to take turn
            print("------------------------------")
            print(str(player.name) + "'s Turn (Your Action)")
            print(str(enemy.name)+" Time Left: " + str(etimer))
            print("------------------------------")
            time.sleep(1)
            while(True):#try-catch block to take input for player actions
                try:
                    print()
                    player.display_actions()
                    print()
                    print(">>>>> YOU [^^Actions Above^^]:")
                    player.display_status()
                    print()
                    print(">>>>> TARGET:")
                    enemy.display_status()
                    print()
                    paction = int(input("Enter Action:"))
                    if paction != int(paction):
                        raise ValueError
                    if paction < 0 or paction >= len(player.skills):
                        raise ValueError
                    break
                except TypeError:
                    print("Not a skill number. Please try again.")
                    print()
                except ValueError:
                    print("Not a skill number. Please try again.")
                    print()
            player.b_action(paction, enemy) #execute action
            ptimer = 1000 #resetting the timer

        if etimer <= 0 and (int(enemy.hp)>0):
            print("------------------------------")
            print(str(enemy.name) + "'s Turn")
            print(str(player.name)+" Time Left: " + str(ptimer))
            print("------------------------------")
            time.sleep(1)
            enemy.display_status()
            time.sleep(1)
            #makes the enemy take a random action
            if len(enemy.skills) > 1:
                eaction=random.randint(0, (len(enemy.skills)-1)) #random part here
            else:
                eaction=0
            enemy.b_action(eaction, player) #execute action
            etimer=1000 #resetting the timer

    if int(player.hp)>0:        #win  <:^)
        print("Victory!")
        enemy.drop_loot(player)
        return True
    else:                       #lose >:^(
        print("Game Over...")
        return False
