// Assingment 9

btn1 = document.getElementById('btn1');
btn2 = document.getElementById('btn2');

function changeColor(color){
    document.getElementById("p1").style.color = color;
}

btn1.addEventListener('click', ()=>{
    document.getElementById("p1").style.color = "red";
});

btn2.addEventListener('click', ()=>{
    document.getElementById("p1").style.color = "blue";
});