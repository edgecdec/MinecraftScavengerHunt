from ScavengerConstants import *

def generateCheckIfAnyoneFinishedFile():
    """
    generates the check if anyone finished file for the datapack
    """
    checkIfFinishCommand = '# Check if anyone has just finished\n'
    checkIfFinishCommand += 'execute as @a[distance=..5,scores={TreasuresLeft=..0},tag=!finished] run say HAS COMPLETED THE SCAVENGER HUNT!\n\n'

    oneTimeCelebrationCommand = '# If anyone has just finished, congratulate them\n'
    oneTimeCelebrationCommand += 'execute as @a[distance=..5,scores={TreasuresLeft=..0},tag=!finished] run summon firework_rocket ~ ~3 ~ {LifeTime:20,FireworksItem:{id:firework_rocket,Count:1,tag:{Fireworks:{Flight:2,Explosions:[{Type:1,Flicker:0,Trail:1,Colors:[I;8073150,14602026],FadeColors:[I;14602026]}]}}}}\n\n'

    addFinishedTagCommand = '# Add the finished tag to anyone who has finished to prevent multiple celebrations\n'
    addFinishedTagCommand += 'tag @a[distance=..5,scores={TreasuresLeft=..0},tag=!finished] add finished\n\n'

    increaseRankOfFinishedPlayersCommand = '# Add 1 to rank of all players who have finished\n'
    increaseRankOfFinishedPlayersCommand += 'execute as @a[tag=finished, scores={TreasuresLeft=..0}] run scoreboard players add @s ScavengerRanking 1\n\n'

    with open(f'{SCAV_FUNCTION_DIR_PATH}control/see_if_anyone_finished.mcfunction', 'w+') as outfile:
        outfile.write(f'{checkIfFinishCommand}{oneTimeCelebrationCommand}{addFinishedTagCommand}{increaseRankOfFinishedPlayersCommand}')
    outfile.close()
