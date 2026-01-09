const time_area = document.getElementById("time-area");

async function get_time(){
    try{
        const res = await fetch("http://127.0.0.1:3000/get-time");
        const time = await res.json()
        time_area.innerHTML = time.time.toUpperCase()
    }catch(err){
        console.log(err)
    }
}

setInterval(get_time,1000)