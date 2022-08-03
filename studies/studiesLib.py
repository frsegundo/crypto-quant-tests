import json

def getDataFromJson(jsonAdd):
    # from json adress, retrieve data information
    tmp = open(jsonAdd)
    data = json.load(tmp)
    tmp.close()

    return data