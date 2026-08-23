import requests
from services.config import RGAPI
from services.get_championData import getChampData
from services.get_lol_puuid import getSummonerPuuid

def getChampMasterybyPUUID(puuid: str, champID: int):
    url = f"https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champID}?api_key={RGAPI}"
    response = requests.get(url)
    data = response.json()

    return (
        data["championLevel"],
        data["championPoints"],
        data["championPointsUntilNextLevel"]
        )
