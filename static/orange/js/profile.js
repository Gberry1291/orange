let navoptions= document.getElementsByClassName("mininavitem")
let pages= document.getElementsByClassName("page")
const orgpages= document.querySelectorAll(".orgpage")
const makerequestbuttons=document.querySelectorAll(".makerequest")
const pulls=document.querySelectorAll(".pullinfo")
var info = JSON.parse(document.getElementById('orgdic').textContent);
var eventdic = JSON.parse(document.getElementById('eventdic').textContent);

for (var i = 0; i < navoptions.length; i++) {
  let j=i
  navoptions[i].addEventListener("click",function(){
    for (var k = 0; k < pages.length; k++) {
      pages[k].classList.remove("selected")
      navoptions[k].classList.remove("mininavselected")
    }
    pages[j].classList.add("selected")
    navoptions[j].classList.add("mininavselected")
  })
}

const newOrgFormTog=document.querySelectorAll(".togneworg")
newOrgFormTog.forEach((item) => {
  item.addEventListener("click",function(){
    document.getElementById("neworgformwindow").classList.toggle("selected")
  })
});
makerequestbuttons.forEach((item) => {
  item.addEventListener("click",sendinfo)
});

function orgPageReset(){
  orgpages.forEach((item) => {
    item.classList.remove("selected")
  });
}


var cleartog=0
let myTimeout
searchinput=document.getElementById("searchinput")
searchinput.addEventListener("input",searchit);
function searchit() {

  if (searchinput.value.length>0) {
    $("#searchcontent").animate({
      "height":"60vh"
    },200,"linear")
  }else {
    $("#searchcontent").animate({
      "height":"0%"
    },200,"linear",function(){
        document.getElementById("searchcontent").innerHTML=""
      }
    )
  }

    if (cleartog==1) {
      clearTimeout(myTimeout);
      myTimeout = setTimeout(firstsearch, 200);
    }else{
      myTimeout = setTimeout(firstsearch, 200);
      cleartog=1
    }

}

function firstsearch(){

    if (searchinput.value.length>0) {

      cleartog=0

      document.getElementById("searchcontent").innerHTML=""
      let word=document.getElementById("searchinput").value;
      let re = new RegExp(word, 'gi');
      let finallist=[]
      for (var i = 0; i < info["orgs"].length; i++) {
        if (match = re.exec(info["orgs"][i]["name"])) {
          finallist.push(info["orgs"][i])
        }
      }
      for (var i = 0; i < finallist.length; i++) {
          let newhouse=document.createElement("div")
          newhouse.className="searchelement"

          let newname=document.createElement("div")
          newname.className="center"
          newname.innerHTML=finallist[i]["name"]

          newhouse.appendChild(newname)

          let sendit=finallist[i]
          newhouse.addEventListener("click",function(){
            searchresultclick(sendit)
          })
          document.getElementById("searchcontent").appendChild(newhouse)

      }

    }

}

var clubname=""
var type=""
var person=""
var whattodo=""
var whattodowith=""
function searchresultclick(orgname){
  searchinput.value=""
  searchit()
  orgPageReset()
  document.getElementById('requestorgpage').classList.add("selected")
  document.getElementById("requestmembertext").innerHTML="Request to Join "+orgname["name"]
  document.getElementById("visitclub").href=extension+"/"+"org/"+orgname["slug"]
  clubname=orgname["name"]
  type="member_request"
}
document.getElementById("closesearch").addEventListener("click",function(){
  orgPageReset()
  document.getElementById("myorgpage").classList.add("selected")
})

pulls.forEach((item) => {
  item.addEventListener("click",pullinfo)
});

function pullinfo(){
  document.getElementById("pushwindow").classList.add("selected")
  document.getElementById("pulltext").innerHTML=this.getAttribute('data-text').replaceAll("-"," ")

  clubname=this.getAttribute('data-club')
  type=this.getAttribute('data-type')
  person=this.getAttribute('data-name')
  whattodo=this.getAttribute('data-whattodo')
  whattodowith=this.getAttribute('data-whattodowith')

}
function andnow(){
  if (whattodo=="delete") {
    document.getElementById(whattodowith).remove()
  }
  clubname=""
  type=""
  person=""
  whattodo=""
  whattodowith=""
}
document.getElementById("confirmpush").addEventListener("click",function(){
  document.getElementById("pushwindow").classList.remove("selected")
  sendinfo()
})
document.getElementById("cancelpush").addEventListener("click",function(){
  document.getElementById("pushwindow").classList.remove("selected")
  clubname=""
  type=""
  person=""
  whattodo=""
  whattodowith=""
})
function sendinfo(){
  path=extension+"/sendinfo"
  whattosend=JSON.stringify({"name":clubname,"type":type,"person":person})

  setreq()
  fetch(newreq).then(function(response) {
    return response.json()
  }).then(function(x) {
    alert(x["message"])
    andnow()
  });
}

document.getElementById("submitorg").addEventListener("click",function(event){
  event.preventDefault()
  checkorgform()
})
function checkorgform(){
  let passed=true
  let inputs = document.getElementsByClassName("orgrequired")
  for (var i = 0; i < inputs.length; i++) {
    if (inputs[i].value=="") {
      inputs[i].classList.add("alertinput")
      inputs[i].placeholder=inputs[i].placeholder+" is required"
      passed=false
    }else {
      inputs[i].classList.remove("alertinput")
    }
  }
  if (passed) {
    document.getElementById('neworgform').submit()
  }
}
const editbuttons=document.querySelectorAll(".edit")
editbuttons.forEach((item) => {
  item.addEventListener("click",filleditform)
});
function filleditform(){
  let club=this.getAttribute('data-name')
  document.getElementById('nameinput').value=eventdic[club]["name"]
  document.getElementById('descriptioninput').value=eventdic[club]["description"]
  document.getElementById('descriptionshortinput').value=eventdic[club]["description_short"]
  document.getElementById('additionalinfoinput').value=eventdic[club]["additional_info"]
  document.getElementById('priceinput').value=eventdic[club]["price"]
  document.getElementById('linkinput').value=eventdic[club]["link_to_external_site"]
  document.getElementById('linktoinput').value=eventdic[club]["link_button_text"]

}


document.getElementById("loadpic").addEventListener("change",function(){
  var file = document.getElementById('loadpic').files[0];
  var reader  = new FileReader();
  // it's onload event and you forgot (parameters)
  reader.onload = function(e)  {
      image=document.getElementById('picloader')
      image.src = e.target.result;
   }
   // you have to declare the file loading
   reader.readAsDataURL(file)
   document.getElementById("profilesave").classList.add("selected")
   togpics()
})
document.getElementById("username").addEventListener("input",function(){
  document.getElementById("profilesave").classList.add("selected")
})
let loadhouses=document.querySelectorAll(".loadhouse")
function togpics(){
  loadhouses.forEach((item) => {
    item.classList.toggle("selected")
  });
}
document.getElementById("delpic").addEventListener("click",function(){
  togpics()
  image=document.getElementById('picloader')
  image.src = extension+"/static/orange/css/propics/guest.png";
  document.getElementById("blank").value="delete"
  document.getElementById("profilesave").classList.add("selected")
})

document.getElementById("emailbutton").addEventListener("click",sendemail)
function sendemail(){
  let theval=document.getElementById('listselect').value.split("<G>")
  let thesub=document.getElementById("messagesubject").value
  let thehead=document.getElementById("messageheader").value
  let thetext=document.getElementById("messagetext").value
  path=extension+"/sendemail"
  whattosend=JSON.stringify(
    {
      "name":theval[1],
      "type":theval[0],
      "sub":thesub,
      "head":thehead,
      "bod":thetext,
    })



  setreq()
  fetch(newreq).then(function(response) {
    return response.json()
  }).then(function(x) {
    alert(x["message"])
  });
}
