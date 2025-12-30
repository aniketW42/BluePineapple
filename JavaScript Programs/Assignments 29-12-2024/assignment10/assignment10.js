// Assingment 10
let count = 1
const btn = document.getElementById("change-img");
btn.addEventListener('click', ()=>{
    const img = document.getElementById("img");
    img.src = img.src.includes("img1.png") ? "img2.png" : "img1.png";  

    btn.textContent = `Image changed * ${count++}`;

})


