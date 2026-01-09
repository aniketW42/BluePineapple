item_list = document.getElementById("item-list")


async function get_menu() {
  try {
    const response = await fetch("http://localhost:3000/menu/get-menu");
    const data = await response.json();
    // console.log(data)
    for(item of data){    
        if(item.id != undefined){
            item_list.innerHTML+= `
                <li class="list-group-item d-flex align-items-start">
                    <img 
                        src="http://localhost:3000/images/${item.image}" 
                        alt="${item.item_name}"
                        class="rounded me-2 m-1"
                        width="60"
                        height="60"
                        style="object-fit: cover;"
                    >

                    <div class="flex-grow-1">
                        <div class="fw-bold">${item.item_name}</div>

                        <p class="mb-1 text-muted text-truncate" style="max-width: 350px;">
                            ${item.description}
                        </p>

                        <span class="badge bg-warning text-dark rounded-pill">
                            ₹${item.price}
                        </span>
                    </div>

                    <div class="d-flex gap-1 ms-3">
                        <button onClick="editItem('${item.id}')" type="button" class="btn btn-warning btn-sm">Edit</button>
                        <button onClick="deleteItem('${item.id}')" type="button" class="btn btn-danger btn-sm">Delete</button>
                    </div>
                </li>

            `
        }
    }

  } catch (err) {
    console.error("Failed to fetch time:", err);
  }
}
get_menu()

async function editItem(id){

    document.getElementById('add-item-modal').classList.remove('d-none');
    document.getElementById('modal-header').textContent = "Edit Item";
    const response = await fetch(`http://localhost:3000/menu/get-menu/${id}`);
    const item = await response.json();
    document.getElementById('item-id').textContent = id;
    document.getElementById("item-name").value = item.item_name;
    document.getElementById("description").value = item.description;
    document.getElementById("price").value = item.price;


}


document.getElementById("item-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const formdata = new FormData();

  formdata.append("item_name", document.getElementById("item-name").value);
  formdata.append("image", document.getElementById("image").files[0]);
  formdata.append("description", document.getElementById("description").value);
  formdata.append("price", document.getElementById("price").value);
  

  if (document.getElementById('modal-header').textContent == "Edit Item"){
    try{
      const id = document.getElementById('item-id').textContent

      const res = await fetch(`http://localhost:3000/menu/edit-item/${id}`, {
          method: "PUT",
          body: formdata
      });

    } catch (err) {
      console.error("Error:", err);
    }
  }else{
    try{
      const res = await fetch("http://localhost:3000/menu/add-item", {
          method: "POST",
          body: formdata
      });
    } catch (err) {
      console.error("Error:", err);
    }
  }

  
});

async function deleteItem(id){
  if( confirm("Are you sure you want to delete this item?")) {
    const res = await fetch(`http://localhost:3000/menu/delete-item/${id}`,{
        method: "DELETE"
    })
  }
}