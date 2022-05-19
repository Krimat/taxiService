import json


CONFIG_FILE = 'taxi_service/settings/config.json'


with open(file=CONFIG_FILE, mode='r') as fin:
    config = json.load(fin)

    if 'PROD' in config:
        from .prod import *
        SECRET_KEY = config['PROD']['SECRET_KEY']
    else:
        from .dev import *
