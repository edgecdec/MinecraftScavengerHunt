from ScavengerConstants import *

# Generate all the files
def generateItemsToFindFiles(itemDict):
    """
    generates the files for what happens when you find each item
    """
    for item in itemDict:
        itemName = item['item']

        itemTellrawColor = 'red'
        if item['tellrawColor'] != '':
            itemTellrawColor = item['tellrawColor']

        itemTag = item['tag']

        # Seperated out to allow for easier changes
        entitiesToGiveTo = f"@a[distance=..{DEFAULT_DISTANCE},tag=!{itemTag},team=ScavengerHunt]"
        executeAsRunCommandPart = f'execute as {entitiesToGiveTo} run'

        giveItemBookCommand = ''
        if item['bookContents'] != '':
            giveItemBookCommand = '# Give player a book\n'
            giveItemBookCommand += f'{executeAsRunCommandPart} give @s written_book{item["bookContents"]}\n\n'

        giveItemMapCommand = ''
        if item['mapID'] != '':
            giveItemMapCommand = '# Give player a map\n'
            giveItemMapCommand += f'{executeAsRunCommandPart} give @s filled_map{{map:{item["mapID"]}}}\n\n'

        giveItemHeadCommand = ''
        if item['headPlayerName'] != '':
            giveItemHeadCommand = '# Give player a head\n'
            giveItemHeadCommand += f'{executeAsRunCommandPart} give @s player_head{{SkullOwner:{item["headPlayerName"]}}}\n\n'

        giveItemCommand = '# Found a treasure\n'
        itemNBT = item['nbt']
        giveItemCommand += f'{executeAsRunCommandPart} give @s {itemName}'
        if itemNBT != '':
            giveItemCommand += itemNBT
        giveItemCommand += '\n\n'

        soundCommand = '# Play sound to user indicating they have found an item\n'
        soundCommand += f'{executeAsRunCommandPart} playsound block.note_block.bell block @s ~ ~ ~ 5 0 1\n\n'

        tellCommand = '# Tell user the item they have found\n'
        tellCommand += f'{executeAsRunCommandPart} title @s title ["", {{"text": "You found "}},{{"text": "a {itemName}!", "bold": true, "color": "{itemTellrawColor}"}}]\n\n'

        treasureLeftCommand = '# subtract 1 from treasures left\n'
        treasureLeftCommand += f'{executeAsRunCommandPart} scoreboard players remove @s TreasuresLeft 1\n\n'

        extraFunctionCommand = ''
        if item['function'] != '':
            extraFunctionCommand = '# execute extra function with other commands\n'
            extraFunctionCommand += f'{executeAsRunCommandPart} function scavenger:extras/{item["function"]}\n\n'

        tagAddCommand = '# add tag indicating they found the treasure\n'
        tagAddCommand += f'{executeAsRunCommandPart} tag @s add {itemTag}\n\n'

        finishCommand = '# check to see if anyone has won\n'
        finishCommand += 'function scavenger:control/see_if_anyone_finished\n\n'

        with open(f'{SCAV_FUNCTION_DIR_PATH}items/scavenger_found_{itemTag}.mcfunction', 'w+') as outfile:
            outfile.write(
                f'{giveItemCommand}'
                f'{giveItemMapCommand}'
                f'{giveItemBookCommand}'
                f'{giveItemHeadCommand}'
                f'{soundCommand}'
                f'{tellCommand}'
                f'{treasureLeftCommand}'
                f'{extraFunctionCommand}'
                f'{tagAddCommand}'
                f'{finishCommand}'
            )
        outfile.close()
