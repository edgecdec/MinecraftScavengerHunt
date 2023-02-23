import zipfile
import os

def putStringOnMultipleLines(inputStr, maxLength = 30, textColor = "gold"):
    curLineLen = 0
    strList = inputStr.split(' ')
    beginStrPart = '\'[{"text":"'
    endStrPart = f'","italic":false,"color":"{textColor}"}}]\''
    outputStr = beginStrPart
    for curStr in strList:
        if(curLineLen == 0 or curLineLen + len(curStr) <= maxLength):
            curLineLen += len(curStr)
            outputStr += f"{curStr} "
        else:
            curLineLen = len(curStr)
            outputStr += f"{endStrPart},{beginStrPart}{curStr} "
    return f"{outputStr}{endStrPart}"

def getArrowName(val):
    if(val == 's'):
        return 'spectral_arrow'
    else:
        return 'arrow'

def getCustomModelData(weaponData):
    tool = weaponData['minecraftToolName']
    if tool == "scute":
        return f"CustomModelData:{weaponData['customModelData']}, "
    else:
        return ""

def zipDir(inputPath, outputFile):
    # ziph is zipfile handle
    ziph = zipfile.ZipFile(outputFile, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(inputPath):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(outputFile, '..')))
    ziph.close()

def setItemTags(scavDict):
    for item in scavDict:
        if item['tag'] == '':
            item['tag'] = item['item']


def runFileEveryXSeconds(functionPath, time):
    '''If you use this you still need to add the fucntion to tick.mcfunction'''
    pass
