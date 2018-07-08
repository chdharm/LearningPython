def jsonDumb(data):
    if type(data) == str or type(data) == unicode:
        return "\"" + str(data) + "\""
    elif type(data) == int or type(data) == float:
        return str(data)
    elif type(data)==list:
        return
    elif type(data)==dict:
        return
    else:
        raise Exception("invalid json value type")