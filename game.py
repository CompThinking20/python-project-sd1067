import random
import time
import source as sgs
import combat as combat
import rooms as rooms
import tags as tags

A1=sgs.skill("Attack", 1, 0, "PHY")#default skills
M1=sgs.skill("Cast", 1, "Drain" , "MAG")#default skills
choices={0:"Fighter", 1:"Mage", 2:"Assassin", 3:"Arcanist"}#for later
room_c=["c","e","g","h"]#for later
gstatus=True#keeps game running

while (gstatus==True):#keeps game running
  name=input("Enter your name:")#asking for a name 
  print("Choose a starting path:")#ask player for starting stats and growth
  print("Fighter(0), Mage(1), Assassin(2), Arcanist(3)")
  while True:#making sure input is correct
    try: 
      choice=int(input("Choice:"))
      if (0 <= choice <= 3)==False:
        raise ValueError
      break
    except TypeError:
      print("Not a valid input. Please try again.")
      print()
    except ValueError:
      print("Not a valid input. Please try again.")
      print()
  #setting everything up for creation
  base_stats=tags.classes[choices[choice]]
  base_growths=tags.class_growths[choices[choice]]
  hp=base_stats[0]
  atk=base_stats[1]
  df=base_stats[2]
  mag=base_stats[3]
  agl=base_stats[4]
  player=sgs.character(name, hp, atk, df, mag, agl)#character is made
  player.add_growths(base_growths)#adds growths from earlier
  #adding default skills
  player.add_skill(A1,"n")
  player.add_skill(M1,"n")
  print("Character Created!")#giving user feedback
  player.level_up(4)
  print()
  player.display_all()
  print()
  input("Press Enter to begin...")#require input to move on
  floor=1#set this here
  while(gstatus==True):#real game loop
    if floor%10 == 0:#every 10 floors is a boss room
      print()
      print("Floor "+str(floor))
      print()
      room1=rooms.room("b",floor)
      room1.display()
      input("Press enter to begin the battle...")
      gstatus=room1.enter(player)
    else:
      random.seed()
      print()
      print("Floor "+str(floor))
      print()
      room1=rooms.room("c",floor)#always will be a combat choice
      r2choice=random.choice(room_c)
      room2=rooms.room(r2choice,floor)#other room will be random
      print("Choose a door:")#player choice
      print("(0)")
      room1.display()
      print("(1)")
      room2.display()
      print()
      while True:#try-catch block for inputs again
        try: 
          choice=int(input("Choice:"))
          if (0 <= choice <= 1)==False:
            raise ValueError
          break
        except TypeError:
          print("Not a valid input. Please try again.")
          print()
        except ValueError:
          print("Not a valid input. Please try again.")
          print()
      if choice==0:
          input("Press enter to begin the encounter...")
          gstatus=room1.enter(player)#enter room
      elif choice==1:
          input("Press enter to begin the encounter...")
          gstatus=room2.enter(player)#enter room
    floor=floor+1#floor rises at end



  