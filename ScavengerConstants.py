import csv

DEFAULT_DISTANCE = 5
PACK_FORMAT_NUM = 5

SCAV_BASE_PATH = 'scavenger_autogen/'
SCAV_FUNCTION_DIR_PATH = f'{SCAV_BASE_PATH}data/scavenger/functions/'

AUTHORS = ['edge_dec', 'XtremeGumdrop']

PLAYING_TEAM_NAME = "ScavengerHunt"
FINISHED_TEAM_NAME = "ScavengerFin"

SCAV_DICT = [row for row in csv.DictReader(open("ScavengerInfo.csv"))]

NUM_ITEMS = len(SCAV_DICT)
