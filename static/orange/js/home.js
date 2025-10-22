const selects= document.querySelectorAll(".fullfilldate")
const events=document.querySelectorAll(".event")
selects.forEach((item) => {
  item.addEventListener("change",filterEvents)
});

var theday=document.getElementById("dayselect")
var themonth=document.getElementById("monthselect")
var theyear=document.getElementById("yearselect")

function filterEvents(){

  events.forEach((item) => {

    item.classList.remove("hide")

    if (item.getAttribute('data-day')!=theday.value && theday.value!="none") {
      item.classList.add("hide")
    }

    if (item.getAttribute('data-month')!=themonth.value && themonth.value!="none") {
      item.classList.add("hide")
    }

    if (item.getAttribute('data-year')!=theyear.value && theyear.value!="none") {
      item.classList.add("hide")
    }

  });

}

// document.getElementById("resetdate").addEventListener("click",resetFilter)
function resetFilter(){
  events.forEach((item) => {
    item.classList.remove("hide")
  })
  theday.value="none"
  themonth.value="none"
  theyear.value="none"
}
