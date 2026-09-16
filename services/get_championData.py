import requests

url = "https://ddragon.leagueoflegends.com/cdn/16.16.1/data/en_US/champion.json"
response = requests.get(url)
database = response.json()

def treatChampName(champName: str):
    cleaned = champName.strip()
    special_cases = {
        "k'sante": "KSante",
        "ksante": "KSante",
        "wukong": "MonkeyKing",
        "leblanc": "Leblanc",
        "dr. mundo": "DrMundo",
        "dr mundo": "DrMundo",
        "drmundo": "DrMundo",
        "renata glasc": "Renata"
    }

    key = cleaned.lower()
    if key in special_cases:
        return special_cases[key]

    clean_name = cleaned.replace("'", "").replace("-", "")
    return "".join(word.capitalize() for word in clean_name.split())

def getChampData(champName: str):
    champFullData = database["data"][treatChampName(champName).strip()]
    return champFullData["key"]
