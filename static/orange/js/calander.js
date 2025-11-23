let date = new Date();
let year = date.getFullYear();
let month = date.getMonth();

var eventinfo = JSON.parse(document.getElementById('alldays').textContent);

const day = document.querySelector(".calendar-dates");
const currdate = document.querySelector(".calendar-current-date");
const prenexIcons = document.querySelectorAll(".calendar-navigation");
const am = document.getElementById("am")
const pm = document.getElementById("pm")

const months = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];

let clickedDay = null;
let selectedDayElement = null;
const manipulate = () => {
  let dayone = new Date(year, month, 1).getDay();
  let lastdate = new Date(year, month + 1, 0).getDate();
  let dayend = new Date(year, month, lastdate).getDay();
  let monthlastdate = new Date(year, month, 0).getDate();

  let daycount=0

  let lit = "";

  for (let i = dayone; i > 0; i--) {
    daycount+=1
    let thedate=i+"-"+(month-1)+"-"+year
    if (eventinfo[thedate]) {
      lit += `<div class="day inactive" data-month="${month-1}" data-year="${year}" data-day="${monthlastdate - i + 1}"> <div class="center">${monthlastdate - i + 1}</div> </div>`
      for (let [key, value] of Object.entries(eventinfo[thedate]["events"])) {
          lit += `<div class="fullfill eventhouse"><div class="center">${value[0]}</div></div>`
      }
      lit += `</div>`

    }else{
      lit += `<div class="day inactive" data-month="${month-1}" data-year="${year}" data-day="${monthlastdate - i + 1}"> <div class="center">${monthlastdate - i + 1}</div> </div>`;
    }
  }


  for (let i = 1; i <= lastdate; i++) {

    daycount+=1

    let isToday = (i === date.getDate()
      && month === new Date().getMonth()
      && year === new Date().getFullYear()) ? "active" : "";

    let thedate=i+"-"+(month+1)+"-"+year

    if (eventinfo[thedate]) {

      lit += `<div class="eventday semi" data-day="${i}" data-month="${month+1}" data-year="${year}"> <div class="fullfill"><div class="center ${isToday}">${i}</div></div>`;

      for (let [key, value] of Object.entries(eventinfo[thedate]["events"])) {
          lit += `<div class="fullfill eventhouse"><div class="center">${value[0]}</div></div>`
      }
      lit += `</div>`

    }else{
      lit += `<div class="day" data-day="${i}" data-month="${month+1}" data-year="${year}"> <div class="center ${isToday}">${i}</div> </div>`;
    }

  }


  for (let i = dayend; i < 6; i++) {

    let thedate=(i - dayend + 1)+"-"+(month+2)+"-"+year
    if (eventinfo[thedate]) {
      lit += `<div class="eventday semi inactive" data-month="${month+2}" data-year="${year}" data-day="${i - dayend + 1}"> <div class="fullfill"><div class="center">${i - dayend + 1}</div> </div>`
      for (let [key, value] of Object.entries(eventinfo[thedate]["events"])) {
          lit += `<div class="fullfill eventhouse"><div class="center">${value[0]}</div></div>`
      }
      lit += `</div>`

    }else{
      lit += `<div class="day inactive" data-day="${i - dayend + 1}" data-month="${month+2}" data-year="${year}"> <div class="center">${i - dayend + 1}</div> </div>`;
    }

    daycount+=1

  }


  day.style.gridTemplateRows = `repeat(${daycount/7},${100/(daycount/7)}%)`;

  currdate.innerText = `${months[month]} ${year}`;
  day.innerHTML = lit;

  addClickListenersToDays();
  addEventDayClicks();
};

var selectedday=""
function addClickListenersToDays() {
  const allDays = day.querySelectorAll('.day');
  allDays.forEach(li => {
    li.addEventListener('click', () => {

      am.innerHTML=""
      pm.innerHTML=""
      let clickedDay = li.getAttribute('data-day');
      let clickedMonth = li.getAttribute('data-month');
      let clickedYear = li.getAttribute('data-year');
      selectedday = (clickedYear+"-"+clickedMonth+"-"+clickedDay)
      for (var i = 1; i < 25; i++) {
        let newhour=document.createElement("div")
        newhour.className="hour free"
        newhour.setAttribute("data-hour", i);
        newhour.addEventListener("click",function(){
          this.classList.toggle("clickedhour");
        })

        let newtime=document.createElement("div")
        newtime.className="center"
        newtime.innerHTML=i+".uhr "+" free"



        newhour.appendChild(newtime)
        if (i<13) {
          am.appendChild(newhour)
        }else {
          pm.appendChild(newhour)
        }
      }
      togday()
    });
  });
}
function addEventDayClicks(){
  const allEventDays = day.querySelectorAll('.eventday');
  allEventDays.forEach(li => {
    li.addEventListener('click', () => {

      let clickedDay = li.getAttribute('data-day');
      let clickedMonth = li.getAttribute('data-month');
      let clickedYear = li.getAttribute('data-year');
      let finallist = (clickedDay+"-"+clickedMonth+"-"+clickedYear)
      selectedday = (clickedYear+"-"+clickedMonth+"-"+clickedDay)
      am.innerHTML=""
      pm.innerHTML=""
      console.log(finallist)
      buildDex(eventinfo[finallist])
      togday()
    });
  });
}
function buildDex(json){

  for (var i = 1; i < 25; i++) {
    let newhour=document.createElement("a")
    let eventname="free"
    if (json["times"][i]=="free") {
      newhour.className="hour free"
      newhour.setAttribute("data-hour", i);
      newhour.addEventListener("click",function(){
        this.classList.toggle("clickedhour");
      })
    }else{
      newhour.className="hour semi"
      eventname=json["events"][json["times"][i]][0]
      newhour.href=extension+"/"+json["events"][json["times"][i]][1]
    }

    let newtime=document.createElement("div")
    newtime.className="center"
    newtime.innerHTML=i+".uhr "+eventname

    newhour.appendChild(newtime)
    if (i<13) {
      am.appendChild(newhour)
    }else {
      pm.appendChild(newhour)
    }
  }

}

manipulate();
prenexIcons.forEach(icon => {
  icon.addEventListener("click", () => {
    month = icon.id === "calendar-prev" ? month - 1 : month + 1;

    if (month < 0 || month > 11) {
      date = new Date(year, month, new Date().getDate());
      year = date.getFullYear();
      month = date.getMonth();
    } else {
      date = new Date();
    }

    clickedDay = null;
    selectedDayElement = null;

    manipulate();
  });
});

let dtogelements=document.getElementsByClassName("togday")
for (var i = 0; i < dtogelements.length; i++) {
  dtogelements[i].addEventListener("click",togday)
}

function togday(){
  document.getElementById('daypage').classList.toggle("selected")
}


var selectedoption="none"
document.getElementById("selecthouse").addEventListener("change",function(event){
  selectedoption=event.target.value
  changeSelectvisibility()
})
var eventhousebuttons=document.getElementsByClassName("eventhousebutton")
function changeSelectvisibility(){
  for (var i = 0; i < eventhousebuttons.length; i++) {
    eventhousebuttons[i].style.display="none"
  }
  if (selectedoption=="newevent") {
    document.getElementById("addeventbutton").style.display="grid"
  }
  if (selectedoption!="newevent" && selectedoption!="none") {
    document.getElementById("saveeventbutton").style.display="grid"
  }
}

document.getElementById("savedaychanges").addEventListener("click",saveday)
function saveday(){

  let daydic={"date":selectedday,"event":selectedoption,"times":[]}

  let clickedhours=document.getElementsByClassName("clickedhour")
  for (var i = 0; i < clickedhours.length; i++) {
    daydic["times"].push(clickedhours[i].getAttribute("data-hour"))
  }

  path=extension+"/saveday"
  whattosend=JSON.stringify(daydic)

  setreq()
  fetch(newreq).then(function(response) {
    return response.json()
  }).then(function(x) {
    eventinfo=x
    manipulate()
    togday()
  });
}
