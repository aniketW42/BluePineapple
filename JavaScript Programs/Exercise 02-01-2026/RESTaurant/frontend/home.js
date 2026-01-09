


document.addEventListener("DOMContentLoaded", () => {
  const time = document.getElementById("time");
  const time2 = document.getElementById("http-time");
  async function get_time() {
    try {
      const response = await fetch("http://localhost:3000/get-time");
      const data = await response.json();
      time.textContent = data.time.toUpperCase();
    } catch (err) {
      console.error("Failed to fetch time:", err);
    }
  }

  async function get_time_http() {
    try {
      const response = await fetch("http://localhost:4000/get-time");
      const data = await response.json(); 
      time2.textContent = data.time.toUpperCase();

    } catch (err) {
      console.error("Failed to fetch time:", err);
    }
  }

  setInterval(get_time, 1000)
  setInterval(get_time_http, 1000)
});