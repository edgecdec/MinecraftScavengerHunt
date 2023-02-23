from ScavengerConstants import *
from datetime import datetime

def generatePackMetaFile():
    """
    generates the pack.mcmeta file for the datapack
    """
    authorStr = f"{', '.join(AUTHORS)} et al."
    curTimeStr = datetime.now().strftime("%m/%d/%Y")

    packFormatLine = f'\t\t"pack_format": {PACK_FORMAT_NUM},\n'
    packDescLine = f'\t\t"description": "Created by {authorStr} on {curTimeStr}"\n'

    packLines = '{\n'
    packLines += '\t"pack": {\n'
    packLines += packFormatLine
    packLines += packDescLine
    packLines += '\t}\n'
    packLines += '}'

    with open(f'{SCAV_BASE_PATH}/pack.mcmeta', 'w+') as outfile:
        outfile.write(packLines)
    outfile.close()
