import sheetdb.helper as helper

class table():
    metadata = ''
    columns = []
    pointer = 0

    def __init__(self, worksheet_object, metadata_exists=False):
        self.worksheet_object = worksheet_object

        if(metadata_exists):
            self.metadata = self._get('A1')
            self.columns = helper.return_columns(self.metadata)
            self.pointer = helper.return_pointer(self.metadata)

    def _update_columns(self, columns):
        self.columns = columns

    def _update_pointer(self, pointer):
        self.pointer = pointer

    def _update_metadata(self, metadata):
        self.metadata = metadata
        self._set('A1', metadata)

    def _set(self, position, value):
        self.worksheet_object.update(position, value)

    def _get(self, position):
        return self.worksheet_object.get(position).first()

    def _set_row(self):
        pass

    def insert(self, values):
        if len(values) != len(self.columns):
            raise Exception('Invalid number of values')

        for value in values:
            if str(type(value)).split("'")[1] != self.columns[values.index(value)][1]:
                raise Exception('Invalid datatype')

        for value in values:
            self._set(helper.return_alpha_index(values.index(value)) + str(3 + self.pointer), value)

        self.pointer += 1
        self._update_metadata(helper.increment_metadata_pointer(self.metadata))
    
    def bulk_insert(self, valuesArray):
        pass
        