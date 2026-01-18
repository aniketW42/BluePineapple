document.addEventListener("DOMContentLoaded", () => {
  const display_time = document.getElementById("time");
  const socket = io("http://127.0.0.1:3000")
  
  socket.on("time", (time)=>{
    display_time.textContent = time.toUpperCase();
  })
  
});
