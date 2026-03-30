async function update_clock() {
    const resHM = await fetch('/clock/H:M');
    if (!resHM.ok) throw new Error("clock error xddd");
    hm = await resHM.text();

    const resS = await fetch('/clock/S');
    if (!resS.ok) throw new Error("clock error xddd");
    s = await resS.text(); //seconds

    document.getElementById("clock").innerHTML = `${hm}<span class="seconds">:${s}</span>`;
}

async function update_weather() {
    const res = await fetch('/weather');
    if (!res.ok) throw new Error("weather error");
    time = await res.text();

    document.getElementById("weather").innerHTML = time;
}

update_clock();
update_weather();
setInterval(update_clock, 1000);
setInterval(update_weather, 600000);