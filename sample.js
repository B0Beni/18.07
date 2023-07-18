// 1. обьявляем переменную let или var
let intNum = 3;
let floatNum = 5.5;
let bool = true;
let str = "сновные цвета";

// 2 . массив
let colors = ["Red", "Green", "Blue"];

// 3. обьявляем функцию
function sayHello(name) {
document.write("Вас зовут: " + name)
}

// 4. идетинфикаторы (айди)
function changeColor(newColor, clicked_id) {
let element = document.getElementById("text");
let rBut = document.getElementById("r");
let gBut = document.getElementById("g");
let bBut = document.getElementById("b");

element.style.color = newColor;

if(clicked_id == "r") {
rBut.style.backgroundColor = newColor;
gBut.style.backgroundColor = '';
bBut.style.backgroundColor = '';
}
else if(clicked_id == "g") {
rBut.style.backgroundColor = '';
gBut.style.backgroundColor = newColor;
bBut.style.backgroundColor = '';
}
else if(clicked_id == "b") {
rBut.style.backgroundColor = '';
gBut.style.backgroundColor = '';
bBut.style.backgroundColor = newColor;
}
}

let name = prompt("Ваше имя");
sayHello(name)