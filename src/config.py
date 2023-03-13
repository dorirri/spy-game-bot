import json
import dotenv

ENV_PATH = '../.env'

DB_FILE = dotenv.get_key(ENV_PATH, 'DB_FILE')
BOT_TOKEN = dotenv.get_key(ENV_PATH, 'BOT_TOKEN')
LOCATIONS_DICT = json.load('../locations.json')