// Top div buttons
const met_select = document.getElementById('met-select');
const eng_select = document.getElementById('eng-select');

// The individual forms themselves
const metric_form = document.querySelector('#metric-form');
const eng_form = document.querySelector('#eng-form');

// The form sections/divs
const met_sect = document.getElementById('met-form-sect')
const eng_sect = document.getElementById('eng-form-sect')

// english units form submission

let submitFormEng = event => {
    event.preventDefault();
    const height_ft = document.querySelector('[name=ft]').value;
    const height_in = document.querySelector('[name=in]').value;
    const weight_lbs = document.querySelector('[name=lb]').value;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    axios({
        method: "POST",
        url: "http://localhost:8000/calculate/eng/",
        headers: {'X-CSRFToken': csrftoken, 'Content-Type': 'application/json'},
        data: {'height_ft': height_ft,
                'height_in': height_in,
                'weight_lbs': weight_lbs,},
    }).then(response => {
        document.getElementById('bmi').innerText = response.data['bmi'];
        console.log(response.data['bmi']);
    }).catch(err => {
        console.log(err)
    })

}
eng_form.addEventListener("submit", submitFormEng, true);

// metric units form submission

let submitFormMet = event => {
    event.preventDefault();
    const height_cm = document.querySelector('[name=cm]').value;
    const weight_kg = document.querySelector('[name=kg]').value;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    axios({
        method: "POST",
        url: "http://localhost:8000/calculate/metric/",
        headers: {'X-CSRFToken': csrftoken, 'Content-Type': 'application/json'},
        data: {'height_cm': height_cm,
                'weight_kg': weight_kg,},
    }).then(response =>{
        document.getElementById('bmi').innerText = response.data['bmi'];
        console.log(response.data['bmi']);
    }).catch(err => {
        console.log(err)
    })

}
metric_form.addEventListener("submit", submitFormMet, true);


// Hide eng form section and grey out the select button when I select metric form
let deactivate = btn => btn.style.background = 'rgb(211, 211, 211)';
let activate = btn => btn.style.background = '#fff';
let hide = sect => sect.style.display = 'none';
let show = sect => sect.style.display = 'block';
met_select.addEventListener("click", () => {
    hide(eng_sect);
    deactivate(eng_select);
    show(met_sect);
    activate(met_select);
    
});
// same thing but vice versa
eng_select.addEventListener("click", () => {
    hide(met_sect);
    deactivate(met_select);
    show(eng_sect);
    activate(eng_select);
    
});

