import os
from dotenv import load_dotenv

import sheetdb

load_dotenv()

token_path = os.getenv('TOKEN_PATH')
key = os.getenv('KEY')