import random
import time
import math
import source as sgs
import combat as combat

#a pool of choices to pull from

#Player choice
classes={
"Fighter":[10,5,4,3,5],
"Mage":[8,2,4,7,3],
"Assassin":[7,6,2,2,9],
"Arcanist":[10,5,4,5,4]
}

class_growths={
"Fighter":[220,160,160,120,140],
"Mage":[180,120,160,190,150],
"Assassin":[170,170,160,120,180],
"Arcanist":[210,120,150,170,150]
}

#enemy Generation
enemy_classes={
"Titan":[170,110,150,110,110],
"Cultist":[120,110,120,160,140],
"Goblin":[150,125,125,125,125],
"Crawler":[150,140,110,110,140],
"Wraith":[120,110,110,170,140],
"Spider":[125,125,125,125,150]
}

enemy_names={
"Fire God's ":[10,120,20,20,30],
"Thunder God's ":[30,50,50,50,110],
"Water God's ":[60,10,35,135,10],
"Wind God's ":[20,30,20,40,120],
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
"Crushing ":"Broken",
0:0,
}

skill_damage={
"Miniscule ":.5,
"Small ":1,
"Medium ":1.5,
"Huge ":2,
"Immense ":2.5,
"Collossal ":3
}

skill_tag={
"God-Blessed ":1,
"Cursed ":-.5,
"Enhanced ":.5,
}
