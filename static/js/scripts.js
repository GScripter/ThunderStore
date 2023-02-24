// Open/Close DropDown
var header = window.document.getElementsByTagName('header')[0]
if(header){
  window.document.getElementById('chk').checked = false
  function dropdown(){
    var chk = window.document.getElementById('chk')
    if(chk.checked){
      window.document.getElementsByClassName('dropdown')[0].style.height = '0px'
    }else{
      window.document.getElementsByClassName('dropdown')[0].style.height = '450px'
    }
  }
}

// Dark Theme
function DarkTheme(){
  localStorage.theme = 'dark'
  window.document.body.classList.add('dark')
  // Icon
  window.document.getElementsByClassName('moon')[0].classList.remove('bi-moon-stars-fill')
  window.document.getElementsByClassName('moon')[0].classList.add('bi-brightness-high')
  window.document.getElementsByClassName('moon')[1].classList.remove('bi-moon-stars-fill')
  window.document.getElementsByClassName('moon')[1].classList.add('bi-brightness-high')
}


// Light Theme
function DefaultTheme(){
  localStorage.theme = 'default'
  window.document.body.classList.remove('dark')
  // Icon
  window.document.getElementsByClassName('moon')[0].classList.remove('bi-brightness-high')
  window.document.getElementsByClassName('moon')[0].classList.add('bi-moon-stars-fill')
  window.document.getElementsByClassName('moon')[1].classList.remove('bi-brightness-high')
  window.document.getElementsByClassName('moon')[1].classList.add('bi-moon-stars-fill')
}


function theme(){
  var ThemeChk = window.document.getElementById('ThemeChk')
  if(ThemeChk.checked){
    DarkTheme()
  }else{
    DefaultTheme()
  }
}


if(localStorage.theme){
  if(localStorage.theme == "dark"){
    DarkTheme()
  }else{
    DefaultTheme()
  }
}


function ShowProductImage(smallImg){
  var fullImg =  document.getElementById("imageBox")
  fullImg.src = smallImg.src;
}


if(localStorage.cookies == null){
  var cookie_alert = window.document.getElementsByClassName("cookie-alert")[0]
  cookie_alert.style.display = "block" 
  var cookies = window.document.getElementById("cookies")
  cookies.addEventListener("click", Cookies)
}

function Cookies(){
  localStorage.cookies = "true"
  var cookies_alert = window.document.getElementsByClassName("cookie-alert")[0]
  cookies_alert.style.display = "none" 
}

