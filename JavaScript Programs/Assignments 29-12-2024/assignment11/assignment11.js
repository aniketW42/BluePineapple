// Assingment 11

const seconds = document.getElementById("sec");
let seconds_count = 10
const colors = ["red","blue","green","yellow","orange","purple","pink","brown","black","gray"];
const interval = setInterval(()=>{

    if (seconds_count<0){
        clearInterval(interval);
        seconds.innerHTML = "Time's up!"
    }else{
        seconds.innerHTML = seconds_count--;
    }

    document.getElementById("sec").style.borderColor = colors[seconds_count];

},1000);


