import requests

sarea_list=None

def getInfo():
    global sarea_list
    url ="https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    respones = requests.get(url)
    respones.text
    data_list = respones.json()
    sarea_temp = set()
    for item in data_list:
        sarea_temp.add(item["sarea"])
    sarea_list = sorted(list(sarea_temp))


getInfo()