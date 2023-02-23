from ScavengerConstants import *

def generateJoinGameFile():
    """
    generates the file which is executed when people join the scavenger hunt
    """
    clearCommand = '# clear inventory\n'
    clearCommand += f'{EXECUTE_AS_NEAREST_PLAYER} clear\n\n'

    scoreboardCreationCommand = '# set scoreboard treasures left to 0\n'
    scoreboardCreationCommand += f'{EXECUTE_AS_NEAREST_PLAYER} scoreboard players set @s TreasuresLeft {str(NUM_ITEMS)}\n\n'

    scoreboardPlayerCommand = '# set finishing rank to 0\n'
    scoreboardPlayerCommand += f'{EXECUTE_AS_NEAREST_PLAYER} scoreboard players set @s ScavengerRanking 0\n\n'

    joinTeamCommand = '# join team\n'
    joinTeamCommand += f'{EXECUTE_AS_NEAREST_PLAYER} team join ScavengerHunt\n\n'

    with open(f'{SCAV_FUNCTION_DIR_PATH}control/join_game.mcfunction', 'w+') as outfile:
        outfile.write(
            f'{clearCommand}'
            f'{scoreboardCreationCommand}'
            f'{scoreboardPlayerCommand}'
            f'{joinTeamCommand}'
        )
    outfile.close()
