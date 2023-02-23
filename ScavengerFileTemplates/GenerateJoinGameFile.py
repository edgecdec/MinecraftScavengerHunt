from ScavengerConstants import *

def generateJoinGameFile():
    """
    generates the file which is executed when people join the scavenger hunt
    """
    clearCommand = '# clear inventory\n'
    clearCommand += 'execute as @p run clear\n\n'

    scoreboardCreationCommand = '# set scoreboard treasures left to 0\n'
    scoreboardCreationCommand += f'scoreboard players set @p TreasuresLeft {str(NUM_ITEMS)}\n\n'

    scoreboardPlayerCommand = '# set finishing rank to 0\n'
    scoreboardPlayerCommand += 'scoreboard players set @p ScavengerRanking 0\n\n'

    joinTeamCommand = '# join team\n'
    joinTeamCommand += 'execute as @p run team join ScavengerHunt\n\n'

    with open(f'{SCAV_FUNCTION_DIR_PATH}control/join_game.mcfunction', 'w+') as outfile:
        outfile.write(f'{clearCommand}{scoreboardCreationCommand}{scoreboardPlayerCommand}{joinTeamCommand}')
    outfile.close()
