# Found a treasure
execute as @a[distance=..5,tag=!cottage2,team=ScavengerHunt] run give @s pumpkin

# Give player a book
execute as @a[distance=..5,tag=!cottage2,team=ScavengerHunt] run give @s written_book{pages:['{"text":"10/28/21\\n\\nWearing: White cashmere sweater, blue jeans, white sneakers. Hair down, no makeup. \\n\\nI took you to the fountain, hoping you would love what I did for you. You didn\'t seem happy. I could see the fear in your eyes. Why are you \\n\\n "}','{"text":"scared of me? You liked my hair. You\'re in love with me. Can\'t you see how devoted I am to you? I even took the time to get rid of your so-called EX boyfriend. You tried to run away, so I had to knock you out :( but dont worry, I made sure not to make not even a scratch on your beautiful face. "}','["",{"text":"If you didn\'t like the place I made for you, "},{"text":"I have no choice but to put you in the cellar.","color":"dark_red"},{"text":"\\n\\nIt\'s not as nice, but you\'re going to love it.","color":"reset"}]','{"text":"You\'re going to love me."}'],title:"Book 3",author:Ted}

# Play sound to user indicating they have found an item
execute as @a[distance=..5,tag=!cottage2,team=ScavengerHunt] run playsound block.note_block.bell block @s ~ ~ ~ 5 0 1

# Tell user the item they have found
execute as @a[distance=..5,tag=!cottage2,team=ScavengerHunt] run title @s title ["", {"text": "You found "},{"text": "a pumpkin!", "bold": true, "color": "red"}]

# subtract 1 from treasures left
execute as @a[distance=..5,tag=!cottage2,team=ScavengerHunt] run scoreboard players remove @s TreasuresLeft 1

# add tag indicating they found the treasure
execute as @a[distance=..5,tag=!cottage2,team=ScavengerHunt] run tag @s add cottage2

# check to see if anyone has won
function scavenger:control/see_if_anyone_finished

