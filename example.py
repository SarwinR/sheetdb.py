import os
from dotenv import load_dotenv

import sheetdb.sheetdb as sheetdb

load_dotenv()

token_path = os.getenv('TOKEN_PATH')
key = os.getenv('KEY')

db = sheetdb.sheetdb(token_path, key)

tb = db.get_table('test')
print(tb.get_all())
#tb = db.create_table('test', [['interger','int'], ['decimal', 'float'], ['string', 'str']])

#for i in range(0,10):
#    tb.insert([999, 1.0, '999'])