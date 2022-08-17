from importlib.metadata import metadata


def return_alpha_index(index):
    #need to add error handling for invalid index
    return chr(65 + index)

def return_metadata(names):
    metadata = ""
    for name in names:
        metadata += name + '~'
    return metadata[:-1]