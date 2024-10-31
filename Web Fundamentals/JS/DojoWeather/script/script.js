// Hide cookies div
function hideDiv() {
    var x = document.getElementById("cookie_div");
    x.style.display = "none";
}

const img1 = document.getElementById('img1');
const img2 = document.getElementById('img2');
const img3 = document.getElementById('img3');
const img4 = document.getElementById('img4');

const desc1 = document.getElementById('desc1');
const desc2 = document.getElementById('desc2');
const desc3 = document.getElementById('desc3');
const desc4 = document.getElementById('desc4');

const temp1h = document.getElementById('temp1h');
const temp1l = document.getElementById('temp1l');
const temp2h = document.getElementById('temp2h');
const temp2l = document.getElementById('temp2l');
const temp3h = document.getElementById('temp3h');
const temp3l = document.getElementById('temp3l');
const temp4h = document.getElementById('temp4h');
const temp4l = document.getElementById('temp4l');
const cityname = document.getElementById('cityname');


function north_PS() {
    img1.src = './icon/sunny.png';
    img2.src = './icon/sunny.png';
    img3.src = './icon/rainy.png';
    img4.src = './icon/cloudy.png';

    cityname.innerText = 'North Palestine'

    desc1.innerText = 'Sunny';
    desc2.innerText = 'sunny';
    desc3.innerText = 'Rainy';
    desc4.innerText = 'Cloudy';

    temp1h.innerText = '23°C';
    temp1l.innerText = '17°C';
    temp2h.innerText = '25°C';
    temp2l.innerText = '19°C';
    temp3h.innerText = '20°C';
    temp3l.innerText = '14°C';
    temp4h.innerText = '22°C';
    temp4l.innerText = '16°C';
}

function jeruslem_PS() {
    img1.src = './icon/sunny.png';
    img2.src = './icon/partly_cloudy.png';
    img3.src = './icon/rainy.png';
    img4.src = './icon/cloudy.png';

    cityname.innerText = 'Jerusalem'


    desc1.innerText = 'Sunny_day';
    desc2.innerText = 'Partly Cloudy';
    desc3.innerText = 'Rainy_day';
    desc4.innerText = 'Cloudy_day';

    temp1h.innerText = '30°C';
    temp1l.innerText = '23°C';
    temp2h.innerText = '22°C';
    temp2l.innerText = '18°C';
    temp3h.innerText = '15°C';
    temp3l.innerText = '10°C';
    temp4h.innerText = '21°C';
    temp4l.innerText = '15°C';
}

function south_PS() {
    img1.src = './icon/cloudy.png';
    img2.src = './icon/rainy.png';
    img3.src = './icon/sunny.png';
    img4.src = './icon/partly_cloudy.png';

    cityname.innerText = 'South Palestine'


    desc1.innerText = 'Cloudy_day';
    desc2.innerText = 'Rainy_day';
    desc3.innerText = 'Sunny_day';
    desc4.innerText = 'Partly Cloudy';

    temp1h.innerText = '22°C';
    temp1l.innerText = '19°C';
    temp2h.innerText = '18°C';
    temp2l.innerText = '10°C';
    temp3h.innerText = '30°C';
    temp3l.innerText = '22°C';
    temp4h.innerText = '24°C';
    temp4l.innerText = '17°C';
}

// Define the convertTemperature function 
function convertTemperature() {
    const select = document.getElementById('temp');
    const selectedValue = select.value;
    // parssInt()
    const temps = [temp1h, temp1l, temp2h, temp2l, temp3h, temp3l, temp4h, temp4l];

    temps.forEach(temp => {
        
        let value = parseInt(temp.innerText);
        if (selectedValue === '°F') {
            value = Math.round((value * 9 / 5) + 32) + "°F";
        } else {
            value = Math.round((value - 32) * 5 / 9) + "°C";
        }
        temp.innerText = value;
    });
}
