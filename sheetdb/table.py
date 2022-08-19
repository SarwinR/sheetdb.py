import sheetdb.helper as helper

class table():
    metadata = ''
    columns = []
    pointer = 0

    operations = ['=', '>', '<', '>=', '<=', '!=']

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

    def _set_row(self, position, values):
        pos = position + ':' + helper.return_alpha_index(len(values) - 1) + position[len(position)-((len(position)-1)):]
        self.worksheet_object.update(pos, [values])

    def insert(self, values):
        if len(values) != len(self.columns):
            raise Exception('Invalid number of values')

        for value in values:
            if str(type(value)).split("'")[1] != self.columns[values.index(value)][1]:
                raise Exception('Invalid datatype')

        self._set_row('A' + str(3 + self.pointer), values)

        self.pointer += 1
        self._update_metadata(helper.increment_metadata_pointer(self.metadata))
    


    def get(self, conditions=[]):
        if(conditions == []):
            return self._get_all()
        else:
            # check if parameters are valid !!!
            return self._get_condition(conditions)

    def _get_condition(self, conditions): 
        data = self.get_all()
        return data

    def _get_all(self):
        raw_values = self.worksheet_object.get_all_values()
        columns = []
        for i in range(len(raw_values[1])):
            columns.append([])

        for row in raw_values[2:]:
            for value in row:
                columns[row.index(value)].append(value)

        column_types = []
        column_names = []
        for value in raw_values[1]:
            column_types.append(value.split(':')[0])
            column_names.append(value.split(':')[1])

        data = {
            'metadata': raw_values[0][0],
            'column_names': column_names,
            'column_types': column_types,
            'rows': raw_values[2:],
            'columns': columns
        }
        return data

        