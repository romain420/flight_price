//recuperation des elements html
//par id
const burger = document.getElementById("burger")
const menu = document.getElementById("menu_burger")
const cross = document.getElementById("cross")
//par type
const body = document.querySelector("body")


//fonction d'affichage du menu
const menu_display = function(){
    burger.style.display = "none"
    menu.style.display = "block"
    cross.style.display = "block"
}

function burger_display(){
    burger.style.display = "block"
    menu.style.display = "none"
    cross.style.display = "none"
}


burger.addEventListener('click', menu_display)
cross.addEventListener("click", burger_display)


