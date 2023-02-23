# clear inventory
execute as @p run clear

# set scoreboard treasures left to 0
execute as @p run scoreboard players set @s TreasuresLeft 5

# set finishing rank to 0
execute as @p run scoreboard players set @s ScavengerRanking 0

# join team
execute as @p run team join ScavengerHunt

