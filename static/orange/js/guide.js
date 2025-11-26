var guidetogelements=document.querySelectorAll(".togguide")
var selectedpage=1
guidetogelements.forEach((item) => {
  item.addEventListener("click",function(){
    document.getElementById("page"+selectedpage).classList.toggle("selected")
  })
});

function nextpage(){
  document.getElementById("page"+selectedpage).classList.toggle("selected");
  selectedpage+=1;
  document.getElementById("page"+selectedpage).classList.toggle("selected");
}
function prevpage(){
  document.getElementById("page"+selectedpage).classList.toggle("selected");
  selectedpage-=1;
  document.getElementById("page"+selectedpage).classList.toggle("selected");
}

var nextnext=document.querySelectorAll(".nextnext")
var prevprev=document.querySelectorAll(".prevprev")
nextnext.forEach((item) => {
  item.addEventListener("click",function(){
    nextpage()
  })
});
prevprev.forEach((item) => {
  item.addEventListener("click",function(){
    prevpage()
  })
});
