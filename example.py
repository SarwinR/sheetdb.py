import os
from dotenv import load_dotenv

import sheetdb.sheetdb as sheetdb

load_dotenv()

token_path = os.getenv('TOKEN_PATH')
key = os.getenv('KEY')

db = sheetdb.sheetdb(token_path, key)
tb = db.create_table('player', [['id','str'], ['name', 'str'], ['age', 'int']])
