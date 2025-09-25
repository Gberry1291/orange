const joinbutton= document.getElementById("joinevent")
joinbutton.addEventListener("click",joinevent)

function joinevent(){
  path=extension+"/orange/sendinfo"
  whattosend=JSON.stringify({"name":joinbutton.getAttribute('data-club'),"type":joinbutton.getAttribute('data-type'),"person":"blank"})

  setreq()
  fetch(newreq).then(function(response) {
    return response.json()
  }).then(function(x) {
    alert(x["message"])
    if (x["check"]=="success") {
      alert(x["message"])
      turnblack()
    }

  });
}
function turnblack(){
  let colorguys=document.querySelectorAll(".batterybodycolor")
  if (joinbutton.getAttribute('data-type')=="attendevent") {
    joinbutton.setAttribute("data-type", "dontattendevent")
    document.getElementById("batterytextoption").innerHTML="Cancel attendance"
    document.getElementById("attendtext").innerHTML="You are Attending, cant make it? no problem."
  }else{
    joinbutton.setAttribute("data-type", "attendevent")
    document.getElementById("batterytextoption").innerHTML="Join Event!"
    document.getElementById("attendtext").innerHTML="Click to rejoin"
  }
  colorguys.forEach((item) => {
    item.classList.toggle("badguycolor")
  });

}
