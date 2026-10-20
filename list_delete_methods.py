def list_delete_methods(lst, method, value=None):
    if method == 'remove':
        lst.remove(value)
    elif method == 'pop':
        if value is None:
            lst.pop()
        else:
            lst.pop(value)
    elif method == 'del':
        del lst[value]
    elif method == 'clear':
        lst.clear()
    else:
        raise ValueError("Invalid method.")

    return lst