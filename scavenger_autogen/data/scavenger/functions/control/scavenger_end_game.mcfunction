# Clear inventories
execute as @a[team=ScavengerHunt] run clear

# Remove Teams
team remove ScavengerHunt
team remove ScavengerFinished

# Remove Scoreboard Objective
scoreboard objectives remove TreasuresLeft
scoreboard objectives remove ScavengerRanking

# Remove Tags
tag @a remove cottage1
tag @a remove cottage2
tag @a remove cottage3
tag @a remove cottage4
tag @a remove iron_axe
tag @a remove finished