def return_alpha_index(index):
    #need to add error handling for invalid index
    return chr(65 + index)

def return_table_creation_metadata(columns):
    metadata = ""
    for column in columns:
        metadata += column[1] + ':' + column[0] + '~'
    return metadata + '0'

def increment_metadata_pointer(metadata):
    md = metadata.split('~')
    md[-1] = str(int(md[-1]) + 1)
    return '~'.join(md)

def return_columns(metadata):
    columns = []
    for column in metadata.split('~'):
        columns.append(column.split(':')[::-1])

    print(columns[:-1])
    return columns[:-1]

def return_pointer(metadata):
    return int(metadata.split('~')[-1])