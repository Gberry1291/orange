var guidetogelements=document.querySelectorAll(".togguide")
guidetogelements.forEach((item) => {
  item.addEventListener("click",function(){
    document.getElementById('guide').classList.toggle("selected")
  })
});

document.getElementById("nextpage").addEventListener("click",nextpage)

function nextpage(){
  document.getElementById('pagetwo').classList.toggle("selected")
  document.getElementById('guide').classList.toggle("selected")
}

document.getElementById("closeguide").addEventListener("click",function(){
  document.getElementById('pagetwo').classList.remove("selected")
  document.getElementById('guide').classList.remove("selected")
})
