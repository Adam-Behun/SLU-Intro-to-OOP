def setDefaultValue(data, key, default):
    if key in data:
        return data[key]
    else:
        data[key] = default
        return default
