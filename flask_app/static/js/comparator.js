const all_flight = document.getElementById("per_day_mean")
const unstop = document.getElementById("per_day_mean_stop")

const all_flight_button = document.getElementById("mean_per_day_allflight")
const unstop_button = document.getElementById("mean_per_day_1stop")

all_flight_button.addEventListener('click', show_mean_day)
unstop_button.addEventListener("click", show_1stop)

all_flight.style.display = 'flex'
unstop.style.display = 'none'

function show_mean_day(){
    all_flight.style.display = 'flex'
    unstop.style.display = 'none'
};

function show_1stop(){
    all_flight.style.display = 'none'
    unstop.style.display = 'flex'
};