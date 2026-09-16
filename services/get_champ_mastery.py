import requests
from services.config import RGAPI
from services.get_championData import getChampData
from services.get_lol_puuid import getSummonerPuuid

def getChampMasterybyPUUID(puuid: str, champID: int):
    url = f"https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champID}?api_key={RGAPI}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 404:
        return (0, 0, 1800)

    if not response.ok:
        print("failed to search champ")

    return (
        data["championLevel"],
        data["championPoints"],
        data["championPointsUntilNextLevel"]
        )
