var etogelements=document.querySelectorAll(".togevent")
etogelements.forEach((item) => {
  item.addEventListener("click",function(){
    document.getElementById('neweventpage').classList.toggle("selected")
  })
});

document.getElementById("submitevent").addEventListener("click",function(event){
  event.preventDefault()
  checkform()
})

function checkform(){
  let passed=true
  let inputs = document.getElementsByClassName("required")
  for (var i = 0; i < inputs.length; i++) {
    if (inputs[i].value=="") {
      inputs[i].classList.add("alertinput")
      inputs[i].placeholder=inputs[i].placeholder+" is required"
      passed=false
    }else {
      inputs[i].classList.remove("alertinput")
    }
  }
  if (document.getElementById('priceinput').value=="") {
    document.getElementById('priceinput').value="free"
  }
  if (passed) {
    console.log("subbed")
    document.getElementById('neweventform').submit()
  }
}
