# Found a treasure
execute as @a[distance=..5,tag=!cottage1,team=ScavengerHunt] run give @s pumpkin

# Give player a book
execute as @a[distance=..5,tag=!cottage1,team=ScavengerHunt] run give @s written_book{pages:['{"text":"10/24/21\\n\\nWhy Wont You Notice mE?\\n\\nWearing: black off-the-shoulder top, black pants, gold jewelry, hair is curled, a hint of brown eyeshadow. I gave you a compliment but you didn\'t hear me. that made me angry. very"}','{"text":"very very very very very very VerY vErY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY VERY angry."}','{"text":"But then I had a whiff of you. You bought a new perfume, which suits you way better than that crappy cheap perfume your boy....boy-friend got. Don\'t worry, I already have my plans to get rid of him. He doesn\'t deserve you at all. "}','["",{"text":"Would he have made a room dedicated to you? no, but I did. "},{"text":"I made it under the water fountain because you like romantic gestures. ","color":"dark_red"},{"text":"I remember small details like that unlike him. I can\'t wait for you to see it. It\'ll be a wonderful surprise.\\n\\n\\n ","color":"reset"}]','["",{"text":"I love you, we "},{"text":"WILL","underlined":true},{"text":" be together soon. ","color":"reset"}]'],title:"Book 2",author:Ted}

# Play sound to user indicating they have found an item
execute as @a[distance=..5,tag=!cottage1,team=ScavengerHunt] run playsound block.note_block.bell block @s ~ ~ ~ 5 0 1

# Tell user the item they have found
execute as @a[distance=..5,tag=!cottage1,team=ScavengerHunt] run title @s title ["", {"text": "You found "},{"text": "a pumpkin!", "bold": true, "color": "red"}]

# subtract 1 from treasures left
execute as @a[distance=..5,tag=!cottage1,team=ScavengerHunt] run scoreboard players remove @s TreasuresLeft 1

# add tag indicating they found the treasure
execute as @a[distance=..5,tag=!cottage1,team=ScavengerHunt] run tag @s add cottage1

# check to see if anyone has won
function scavenger:control/see_if_anyone_finished

