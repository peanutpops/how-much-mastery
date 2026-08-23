import requests
from services.config import RGAPI

def getSummonerPuuid(gameName: str, tagLine: str):
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName.lower()}/{tagLine.lower()}?api_key={RGAPI}"

    response = requests.get(url)
    return response.json()["puuid"]
