from ScavengerConstants import *

def generateSetupGameFile():
    """
    generates the setup game file for the datapack
    """
    createTreasuresLeftCommand = '# adds scoreboard Treasures Left\n'
    createTreasuresLeftCommand += 'scoreboard objectives add TreasuresLeft dummy {"text":"Items Left","bold":true}\n'
    createTreasuresLeftCommand += 'scoreboard objectives add ScavengerRanking dummy {"text":"Scavenger Ranking","bold":true}\n\n'

    createScavHuntTeamCommand = '# adds Scavenger Hunt Team\n'
    createScavHuntTeamCommand += 'team add ScavengerHunt "ScavengerHunt"\n'
    createScavHuntTeamCommand += 'team modify ScavengerHunt color light_purple\n\n'

    createScavHuntFinishTeam = '# add Scavenger Finished Team\n'
    createScavHuntFinishTeam += 'team add ScavengerFin "Scavenger Finished"\n'
    createScavHuntFinishTeam += 'team modify ScavengerFin color dark_blue\n\n'

    addWaitingTagCommand = '# if player has waitingScavenger tag have them join the team\n'
    addWaitingTagCommand += 'execute as @a[tag=waitingScavenger] run team join ScavengerHunt\n\n'

    clearCommand = '# clear player inventory\n'
    clearCommand += 'execute as @a[team=ScavengerHunt] run clear\n\n'

    createUnfoundCommand = '# set all treasures to unfound\n'
    createUnfoundCommand += f'scoreboard players set @a[team=ScavengerHunt] TreasuresLeft {str(NUM_ITEMS)}\n\n'

    displayObjectivePlayingCommand = '# Display objective for players in scavenger hunt\n'
    displayObjectivePlayingCommand += 'scoreboard objectives setdisplay sidebar.team.light_purple TreasuresLeft\n\n'

    displayObjectiveFinishedCommand = '# Display objective for users in scavenger finished team\n'
    displayObjectiveFinishedCommand += 'scoreboard objectives setdisplay sidebar.team.dark_blue ScavengerFin\n\n'

    with open(f'{SCAV_FUNCTION_DIR_PATH}control/scavenger_setup.mcfunction', 'w+') as outfile:
        outfile.write(f'{createTreasuresLeftCommand}{createScavHuntTeamCommand}{createScavHuntFinishTeam}{addWaitingTagCommand}{clearCommand}{createUnfoundCommand}{displayObjectivePlayingCommand}{displayObjectiveFinishedCommand}')
    outfile.close()
