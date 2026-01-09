row = document.getElementById("row")


async function get_menu() {
  try {
    const response = await fetch("http://localhost:3000/menu/get-menu");
    const data = await response.json();
    
    for(item of data){
        if(item.item_name != undefined) {
            let item_div = `
            <div class="card col-12 col-sm-6 col-md-3 " style="width: 18rem;">
                <img 
                  src="http://localhost:3000/images/${item.image}" 
                  class="card-img-top mt-3 rounded border border-warning border-2" alt="img">
                <div class="card-body">
                    <h5 class="card-title">${item.item_name.trim()}</h5>
                    <p class="card-text">
                        ${item.description.trim()}
                    </p>
                </div>
                <p class="badge bg-warning text-black p-2">Rs.${item.price.trim()}</p>
            </div>
            `;
            row.innerHTML = row.innerHTML + item_div;
        }
    }

  } catch (err) {
    console.error("Failed to fetch time:", err);
  }
}

get_menu()