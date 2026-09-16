document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("champion");
    const listContainer = document.getElementById("custom-autocomplete-list");
    const dataElement = document.getElementById("champions-data");

    const CHAMPIONS_DATA = JSON.parse(dataElement.textContent || "[]");

    input.addEventListener("input", function() {
        const value = this.value.trim().toLowerCase();
        listContainer.innerHTML = "";

        if (!value) {
            listContainer.classList.add("hidden");
            return;
        }

        const matches = CHAMPIONS_DATA.filter(champ => 
            champ.name.toLowerCase().includes(value)
        );

        if (matches.length === 0) {
            listContainer.classList.add("hidden");
            return;
        }

        matches.forEach(champ => {
            const item = document.createElement("div");
            item.classList.add("autocomplete-item");

            const iconUrl = `https://ddragon.leagueoflegends.com/cdn/14.8.1/img/champion/${champ.image_key}.png`;

            item.innerHTML = `
                <img src="${iconUrl}" alt="${champ.name}" class="champ-icon" />
                <span>${champ.name}</span>
            `;

            item.addEventListener("click", () => {
                input.value = champ.name;
                listContainer.classList.add("hidden");
            });

            listContainer.appendChild(item);
        });

        listContainer.classList.remove("hidden");
    });

    document.addEventListener("click", (e) => {
        if (!e.target.closest(".autocomplete-container")) {
            listContainer.classList.add("hidden");
        }
    });
});