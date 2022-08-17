def return_alpha_index(index):
    #need to add error handling for invalid index
    return chr(65 + index)

def return_table_creation_metadata(names):
    metadata = ""
    for name in names:
        metadata += name + '~'
    return metadata + '0'

def increment_metadata_pointer(metadata):
    md = metadata.split('~')
    md[-1] = str(int(md[-1]) + 1)
    return '~'.join(md)