# Found a treasure
execute as @a[distance=..5,tag=!iron_axe,team=ScavengerHunt] run give @s iron_axe{display:{Name:'[{"text":"Johnny\'s Axe","italic":false,"color":"yellow"}]',Lore:['[{"text":"May or may not have","color":"#3300cc"}]','[{"text":"belonged to a serial","italic":true,"color":"#3300cc"}]','[{"text":"killer.","italic":true,"color":"#3300cc"},{"text":"","italic":false,"color":"dark_purple"}]','[{"text":"","italic":false,"color":"dark_purple"}]','[{"text":"Halloween 2022","italic":true,"color":"gold"},{"text":"","italic":false,"color":"dark_purple"}]','[{"text":"","italic":false,"color":"dark_purple"}]']},Enchantments:[{id:sharpness,lvl:10},{id:smite,lvl:5}]}

# Play sound to user indicating they have found an item
execute as @a[distance=..5,tag=!iron_axe,team=ScavengerHunt] run playsound block.note_block.bell block @s ~ ~ ~ 5 0 1

# Tell user the item they have found
execute as @a[distance=..5,tag=!iron_axe,team=ScavengerHunt] run title @s title ["", {"text": "You found "},{"text": "a iron_axe!", "bold": true, "color": "red"}]

# subtract 1 from treasures left
execute as @a[distance=..5,tag=!iron_axe,team=ScavengerHunt] run scoreboard players remove @s TreasuresLeft 1

# add tag indicating they found the treasure
execute as @a[distance=..5,tag=!iron_axe,team=ScavengerHunt] run tag @s add iron_axe

# check to see if anyone has won
function scavenger:control/see_if_anyone_finished

