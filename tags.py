import random
import time
import math
import source as sgs
import combat as combat

#Player choice
classes={
"Fighter":[10,5,4,3,5],
"Mage":[8,2,4,7,3],
"Assassin":[7,6,2,2,9],
"Arcanist":[10,5,4,5,4]
}

class_growths={
"Fighter":[120,60,60,20,40],
"Mage":[80,20,60,90,50],
"Assassin":[70,70,60,20,80],
"Arcanist":[110,20,50,70,50]
}

#enemy Generation
enemy_classes={
"Titan":[170,10,50,10,10],
"Cultist":[120,10,20,60,40],
"Goblin":[150,25,25,25,25],
"Crawler":[150,40,10,10,40],
"Wraith":[120,10,10,70,40],
"Spider":[125,25,25,25,50]
}

enemy_names={
"Fire God's ":[10,170,20,20,30],
"Thunder God's ":[30,50,50,50,110],
"Water God's ":[60,10,35,135,10],
"Wind God's ":[20,30,20,40,130],
"Nature God's ":[110,40,50,40,10]
}

enemy_tags={
"Giant ":[50,0,50,0,0],
"Enraged ":[0,100,0,0,0],
"Shining ":[25,0,0,75,0],
"Enchanted ":[20,20,0,40,20],
"Berserk ":[0,75,0,0,25],
"Extreme ":[50,50,50,50,50],
"Agile ":[0,25,0,0,75],
"Protected ":[0,0,60,40,0]
}

#skill generation
skill_primary={
"Slash":"PHY",
"Cast":"MAG",
"Burst":"MAG",
"Bash":"PHY"
}

skill_secondary={
"Vampiric ":"Drain",
"Libra":"Scan",
"Maiming ":"Crippled",
"Exposing ":"Opened",
"Pressure ":"Weakened",
"Crushing ":"Broken"
}

skill_damage={
"Miniscule ":.5,
"Small ":1,
"Medium ":2,
"Huge ":3,
"Immense ":4,
"Collossal ":5
}

skill_tag={
"God-Blessed ":1.5,
"Cursed ":-1,
"Enhanced ":1,
}
