import gspread
import sheetdb.table as table
import sheetdb.helper as helper

class sheetdb():
    datatypes = ['int', 'num', 'str', 'bool']

    def __init__(self, token_path, key):
        self.gc = gspread.service_account(filename=token_path)
        self.sh = self.gc.open_by_key(key)

    def create_table(self, name, columns):
        tb = table.table(self.sh.add_worksheet(name, 0, 0))
        index = 0
        
        for column in columns:
            if column[1] not in self.datatypes:
                raise Exception('Invalid datatype')

            tb.set(helper.return_alpha_index(index) + '1', column[1]+':'+column[0])
            index += 1

        return tb

    def get_table(self, name):
        return table.table(self.sh.worksheet(name))

    def delete_table(self, name):
        worksheet_object = self.sh.worksheet(name)
        self.sh.del_worksheet(worksheet_object)
    