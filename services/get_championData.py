import requests

url = "https://ddragon.leagueoflegends.com/cdn/16.16.1/data/en_US/champion.json"
response = requests.get(url)
database = response.json()

def getChampData(champName: str):
    champFullData = database["data"][champName.capitalize()]
    return champFullData["key"]
