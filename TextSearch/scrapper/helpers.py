def RemoveDuplicateFromList(list):
    ret = []
    for element in list:
        if element not in ret:
            ret.append(element)

    return ret