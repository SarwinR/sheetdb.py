import os
from dotenv import load_dotenv

import sheetdb.sheetdb as sheetdb

load_dotenv()

token_path = os.getenv('TOKEN_PATH')
key = os.getenv('KEY')


db = sheetdb.sheetdb(token_path, key)

tb = db.get_table('test')
#tb = db.create_table('test', [['interger','int'], ['decimal', 'float'], ['string', 'str']])

for i in range(0,25):
    tb.insert([i, 1.1, 'test'])