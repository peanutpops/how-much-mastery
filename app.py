from flask import Flask, render_template, request

from services.get_lol_puuid import getSummonerPuuid
from services.get_championData import getChampData, getAllChampionsForAutocomplete
from services.get_champ_mastery import getChampMasterybyPUUID

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def homepage():
    champNameList = getAllChampionsForAutocomplete()

    if request.method == "GET":
        return render_template("index.html", champNameList=champNameList)
    
    if request.method == "POST":
        riotId = request.form.get("riot_id", "").strip()
        tagLine = request.form.get("tagline", "").strip()
        champName = request.form.get("champion", "").strip()

        try:
            numeric_key, text_id = getChampData(champName)

            if not numeric_key:
                raise ValueError(f"we didn't find this '{champName}' anywhere")
            
            puuid = getSummonerPuuid(riotId, tagLine)
            champLevel, championPoints, pointsUntilNextLevel = getChampMasterybyPUUID(puuid, numeric_key)
            
            if pointsUntilNextLevel <= 0:
                points_remaining = 0
                progress_percent = 100.0
            else:
                points_remaining = pointsUntilNextLevel
                current_level_pts = championPoints % 11000
                total_level_pts = current_level_pts + points_remaining
                
                if total_level_pts > 0:
                    progress_percent = round((current_level_pts / total_level_pts) * 100, 1)
                else:
                    progress_percent = 0.0

            result_data = {
                "riot_id": riotId,
                "tagline": tagLine,
                "champion": champName.title(),
                "mastery_level": champLevel,
                "mastery_points": championPoints,
                "points_remaining": points_remaining,
                "progress_percent": progress_percent,
                "background": f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{text_id}_0.jpg"
            }

            return render_template(
                "index.html", 
                resultado=result_data,
                champNameList=champNameList
            )

        except Exception as e:
            return render_template(
                "index.html", 
                erro=str(e), 
                champNameList=champNameList
            )

if __name__ == "__main__":
    app.run(debug=True)