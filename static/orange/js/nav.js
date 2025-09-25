var startpat=window.location.href
let pattern=/\S*\/\/\S+?(?=\/)/
var extension=startpat.match(pattern)[0];
var newreq=""
var whattosend=""
var path=""
const csrftoken = getCookie('csrftoken');
function setreq(){
  newreq = new Request(
      path,
      {
          method: 'POST',
          headers: {'X-CSRFToken': csrftoken},
          mode: 'same-origin', // Do not send CSRF token to another domain.
          body: whattosend
      }
  );
}
function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";"+"SameSite=None; Secure";
}

var slideitems=document.getElementsByClassName("slideit")
for (var i = 0; i < slideitems.length; i++) {
  slideitems[i].addEventListener("click",slidesignin)
}

var slidetog=0
var togoptions={0:"0%",1:"100%"}
function slidesignin(){
  $("#signslide").animate({
    "left":togoptions[slidetog],
    "width":togoptions[Math.abs(slidetog-1)]
  },300,function(){slidetog = Math.abs(slidetog-1)})
}

document.getElementById("closesigning").addEventListener("click",slidesignin)

const navweekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
const navmonths = [
  "Jan", "Feb", "Mar", "April", "May", "June",
  "July", "Aug", "Sept", "Oct", "Nov", "Dec"
];
function setDate(){
  let date = new Date();
  let day = date.getDate()
  let dayday= navweekday[date.getDay()];
  let month = navmonths[date.getMonth()];
  document.getElementById("monthnav").innerHTML=month
  document.getElementById("daynav").innerHTML=day
  document.getElementById("daydaynav").innerHTML=dayday
}
setDate()
