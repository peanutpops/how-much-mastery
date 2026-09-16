import requests

url = "https://ddragon.leagueoflegends.com/cdn/16.16.1/data/en_US/champion.json"
response = requests.get(url)
database = response.json()

def treatChampName(champName: str):
    if champName.lower() == "wukong":
        return "MonkeyKing"
    treatedString = ""
    listString = champName.split()
    for word in listString:
        treatedString += str(word.capitalize())
    return treatedString

def getChampData(champName: str):
    champFullData = database["data"][treatChampName(champName).strip()]
    return champFullData["key"]
