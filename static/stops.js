//VIBE CODED!!!

const STOP_IDS = [21313, 10813, 10915, 10911];

async function fetchStop(id) {
    const res = await fetch(`/stops/${id}`);
    if (!res.ok) throw new Error("API error");
    return await res.json()
}

async function renderStops(stops) {
    const board = document.getElementById("board");
    board.innerHTML = "";

    stops.forEach(stop => {
        const el = document.createElement("div");
        el.className = "stop";
        
        {
            const name = document.createElement("h1");
            name.className = "stop_name";
            name.innerHTML = stop.name;
            el.appendChild(name);
        }
        {
            const timetable = document.createElement("div");
            timetable.className = "timetable"

            for (const dep of stop.departures) {
                const line = document.createElement("h2");
                line.className = "line";
                line.innerHTML = `<em>${dep.line} ${dep.direction}</em>: ${dep.time}`;
                
                timetable.appendChild(line);
            }
            el.appendChild(timetable)
        }

        board.appendChild(el);
    });
}

async function update() {
    try {
        const data = await Promise.all(
            STOP_IDS.map(id => fetchStop(id))
        );
        console.log(data);
        renderStops(data);
    } catch (err) {
        console.error(err);
        document.getElementById("board").textContent = "failed to load data";
    }
}
update();
setInterval(update, 30000);