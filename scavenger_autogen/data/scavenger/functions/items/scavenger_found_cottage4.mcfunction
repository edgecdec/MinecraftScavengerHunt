# Found a treasure
execute as @a[distance=..5,tag=!cottage4,team=ScavengerHunt] run give @s pumpkin

# Give player a book
execute as @a[distance=..5,tag=!cottage4,team=ScavengerHunt] run give @s written_book{pages:['{"text":"10/31/21 \\n\\nYOU GAVE ME NO CHOICE. \\n\\nWHY DID YOU TRY TO LEAVE? YOU JUST HAD TO ESCAPE THE PLACE I MADE FOR YOU. WE COULD\'VE BEEN HAPPY. WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY "}','{"text":"WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY\\n "}','{"text":"It\'s okay. Regardless, this is a way for us to be together forever. You\'ll always be with me. \\n\\n \\u0020 \\u0020 \\u0020Forever."}'],title:"Book 4",author:Ted}

# Give player a head
execute as @a[distance=..5,tag=!cottage4,team=ScavengerHunt] run give @s player_head{SkullOwner:lotusMMI}

# Play sound to user indicating they have found an item
execute as @a[distance=..5,tag=!cottage4,team=ScavengerHunt] run playsound block.note_block.bell block @s ~ ~ ~ 5 0 1

# Tell user the item they have found
execute as @a[distance=..5,tag=!cottage4,team=ScavengerHunt] run title @s title ["", {"text": "You found "},{"text": "a pumpkin!", "bold": true, "color": "red"}]

# subtract 1 from treasures left
execute as @a[distance=..5,tag=!cottage4,team=ScavengerHunt] run scoreboard players remove @s TreasuresLeft 1

# add tag indicating they found the treasure
execute as @a[distance=..5,tag=!cottage4,team=ScavengerHunt] run tag @s add cottage4

# check to see if anyone has won
function scavenger:control/see_if_anyone_finished

