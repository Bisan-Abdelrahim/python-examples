def delete_dictionary_key(d, key):
    if key in d:
        del d[key]
    return d