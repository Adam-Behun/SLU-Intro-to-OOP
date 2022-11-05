def getDictionaryAsList(data):
    some_list = []
    for key in data:
        some_list.append((key, data[key]))
    return some_list
