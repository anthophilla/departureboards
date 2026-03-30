THIS PROJECT WAS CODED WITH THE HELP OF AI! (sadly)

This is just a quick project i made for my school that will display the departure times and other data of bus/tram stops in Szczecin Poland using the ZDiTM api(it should be realy easy to change the api to yours).

# How to run:
make sure you have all the dependencies installed `python pip uv`
> arch linux:
>> `sudo pacman -S uv`
>
> Ubuntu/Debian
> install [uv](https://github.com/astral-sh/uv) using their standalone installer:
>> `wget -qO- https://astral.sh/uv/install.sh | sh`

clone the repo
>
>``git clone https://github.com/anthophilla/departureboards.git``
>
>``cd departureboards``

create venv and install the pip dependencies
> using uv:
>>
>> `uv venv`
>> `uv pip install flask requests`

finally run the server
> `uv run flask --app main run`
then open `127.0.0.1:5000` in your browser!

# How to add/remove bus/tram stops:

inside `static/stops.js` should be `const STOP_IDS = [...];`
and to add a stop just paste an id inside like this `, 10434`

the zditm stop ids can be found [here](https://www.zditm.szczecin.pl/en/passenger/timetables/map-of-stops-and-vehicles)
<img width="955" height="602" alt="departures" src="https://github.com/user-attachments/assets/ec23a0c5-13ae-48fc-92c9-6cce3f480293" />

# Styling
all styling is cointained in `static/styles.css` and the skeleton for use as reference is `skeleton.html`

# Use with fullpage-os
! Experimental !
1. connect to your device with ssh (this setup was made in mind that the user is pi if the username is different you will need to adjust `departureboards.service` aswell as other steps in this section)
2. use instructions for ubuntu in section *How to run* to install but **dont run the server**.
3. copy the unit file `sudo cp departureboards.service /etc/systemd/system/departureboards.service`
4. refresh systemctl `sudo systemctl daemon-reexec && sudo systemctl daemon-reload`
5. enable the service `sudo systemctl enable busboard`
6. change the url in `/boot/firmware/fullpageos.txt`
7. reboot the device!