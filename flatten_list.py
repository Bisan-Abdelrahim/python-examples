def flatten_list(nested_list):
    result = []

    for sublist in nested_list:
        result = result + sublist

    return result