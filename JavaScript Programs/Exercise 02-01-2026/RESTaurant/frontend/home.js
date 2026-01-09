document.addEventListener("DOMContentLoaded", () => {
  const time = document.getElementById("time");
  async function get_time() {
    try {
      const response = await fetch("http://localhost:3000/get-time");
      const data = await response.json();
      time.textContent = data.time.toUpperCase();
    } catch (err) {
      console.error("Failed to fetch time:", err);
    }
  }

  setInterval(get_time, 1000)
  
});