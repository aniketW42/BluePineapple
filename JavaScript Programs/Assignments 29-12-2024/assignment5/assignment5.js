// Assingment 5

button1 = document.getElementById("button1");

function textChange(){
    document.getElementById("div1").innerHTML = "You clicked the button!";
}

button1.addEventListener('click', textChange);


