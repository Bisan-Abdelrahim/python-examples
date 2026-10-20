def list_memory_address(list1, list2):
    return abs(id(list1) - id(list2))