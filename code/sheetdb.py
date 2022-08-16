import gspread

class table():
    def __init__(self, worksheet_object):
        self.worksheet_object = worksheet_object

    def set(self, position, value):
        self.worksheet_object.update(position, value)

    def get(self, position):
        return self.worksheet_object.get(position).first()

class sheetdb():
    datatypes = ['int', 'num', 'str', 'bool']

    def __init__(self, token_path, key):
        self.gc = gspread.service_account(filename=token_path)
        self.sh = self.gc.open_by_key(key)

    def create_table(self, name):
        return table(self.sh.add_worksheet(name, 0, 0))

    def get_table(self, name):
        return table(self.sh.worksheet(name))

    def delete_table(self, name):
        worksheet_object = self.sh.worksheet(name)
        self.sh.del_worksheet(worksheet_object)
    