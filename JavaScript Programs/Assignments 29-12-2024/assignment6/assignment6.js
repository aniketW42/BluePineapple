// Assingment 6

const add_button = document.getElementById("add-item");
const item_list = document.getElementById("items");

let item_count = 0;

function addItem(){
    item_count = item_count + 1;
    const element = document.createElement("li");
    element.innerHTML = `Item ${item_count}`;
    item_list.appendChild(element);
}

add_button.addEventListener('click', addItem);
