from flask import Flask, render_template, request

from services.get_lol_puuid import getSummonerPuuid
from services.get_championData import getChampData
from services.get_champ_mastery import getChampMasterybyPUUID

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        riotId = request.form.get("riot_id", "").strip()
        tagLine = request.form.get("tagline", "").strip()
        champName = request.form.get("champion", "").strip()

        try:
            puuid = getSummonerPuuid(riotId, tagLine)
            champId = getChampData(champName)
            if not champId:
                raise ValueError(f"we didn't found this '{champName}' anywhere")
            
            champLevel, championPoints, pointsUntilNextLevel = getChampMasterybyPUUID(puuid, champId)
            result_data = {
                "riot_id": riotId,
                "tagline": tagLine,
                "champion": champName.title(),
                "mastery_level": champLevel,
                "mastery_points": championPoints,
                "points_remaining": pointsUntilNextLevel
            }
            return render_template("index.html", resultado=result_data)
        except Exception as e:
            return render_template("index.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)