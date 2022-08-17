import gspread
import sheetdb.table as table
import sheetdb.helper as helper

class sheetdb():
    datatypes = ['int', 'num', 'str', 'bool']

    def __init__(self, token_path, key):
        self.gc = gspread.service_account(filename=token_path)
        self.sh = self.gc.open_by_key(key)

    def create_table(self, name, columns):
        column_names = []
        for column in columns:
            if column[1] not in self.datatypes:
                raise Exception('Invalid datatype')
            
            if column[0] in column_names:
                raise Exception('Duplicate column name')

            column_names.append(column[0])
        
        tb = table.table(self.sh.add_worksheet(name, 0, 0))
        
        index = 0
        for column in columns:
            tb.set(helper.return_alpha_index(index) + '2', column[1]+':'+column[0])
            index += 1

        tb.set('A1', helper.return_metadata(column_names))
        return tb

    def get_table(self, name):
        return table.table(self.sh.worksheet(name))

    def delete_table(self, name):
        worksheet_object = self.sh.worksheet(name)
        self.sh.del_worksheet(worksheet_object)
    