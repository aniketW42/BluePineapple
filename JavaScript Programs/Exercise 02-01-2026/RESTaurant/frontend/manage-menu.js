const itemList = document.getElementById("item-list");
const itemForm = document.getElementById("item-form");
const modal = document.getElementById("add-item-modal");
const modalHeader = document.getElementById("modal-header");

const itemIdEl = document.getElementById("item-id");
const itemNameEl = document.getElementById("item-name");
const descriptionEl = document.getElementById("description");
const priceEl = document.getElementById("price");
const imageEl = document.getElementById("image");

const API_BASE = "http://localhost:3000/menu";

/* FETCH & RENDER MENU */
async function getMenu() {
  try {
    const response = await fetch(`${API_BASE}/get-menu`);
    if (!response.ok) throw new Error("Failed to fetch menu");

    const data = await response.json();
    itemList.innerHTML = "";

    const fragment = document.createDocumentFragment();

    data.forEach((item) => {
      const li = document.createElement("li");
      li.className = "list-group-item d-flex align-items-start";

      li.innerHTML = `
        
        <input type="checkbox" name="tags[]" value="${item.id}" class="p-2 me-1 mt-1">
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
          <button class="btn btn-warning btn-sm edit-btn">Edit</button>
          <button class="btn btn-danger btn-sm delete-btn">Delete</button>
        </div>
      `;

      li.querySelector(".edit-btn").addEventListener("click", () =>
        editItem(item.id)
      );
      li.querySelector(".delete-btn").addEventListener("click", () =>
        deleteItem(item.id)
      );

      fragment.appendChild(li);
    });

    itemList.appendChild(fragment);
  } catch (err) {
    console.error("Error fetching menu:", err);
  }
}

getMenu();

/* EDIT ITEM */
async function editItem(id) {
  try {
    modal.classList.remove("d-none");
    modalHeader.textContent = "Edit Item";

    const response = await fetch(`${API_BASE}/get-menu/${id}`);
    if (!response.ok) throw new Error("Failed to fetch item");

    const item = await response.json();

    itemIdEl.textContent = id;
    itemNameEl.value = item.item_name;
    descriptionEl.value = item.description;
    priceEl.value = item.price;
  } catch (err) {
    console.error("Error loading item:", err);
  }
}

/* ADD / UPDATE ITEM */
itemForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData();
  formData.append("item_name", itemNameEl.value);
  formData.append("description", descriptionEl.value);
  formData.append("price", priceEl.value);

  if (imageEl.files[0]) {
    formData.append("image", imageEl.files[0]);
  }

  const isEdit = modalHeader.textContent === "Edit Item";
  const url = isEdit
    ? `${API_BASE}/edit-item/${itemIdEl.textContent}`
    : `${API_BASE}/add-item`;

  const method = isEdit ? "PUT" : "POST";

  try {
    const response = await fetch(url, { method, body: formData });
    if (!response.ok) throw new Error("Failed to save item");

    resetForm();
    getMenu();
  } catch (err) {
    console.error("Error saving item:", err);
  }
});

/* DELETE ITEM */
async function deleteItem(id) {
  if (!confirm("Are you sure you want to delete this item?")) return;

  try {
    const response = await fetch(`${API_BASE}/delete-item/${id}`, {
      method: "DELETE",
    });

    if (!response.ok) throw new Error("Failed to delete item");

    getMenu();
  } catch (err) {
    console.error("Error deleting item:", err);
  }
}

async function bulkDelete() {
  const selectedIds = Array.from(
    document.querySelectorAll('input[name="tags[]"]:checked')
  ).map((c) => c.value);

  if (!confirm(`Are you sure you want to delete ${selectedIds.length} item?`))
    return;

  try {
    const response = await fetch(`${API_BASE}/bulk-delete`, {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ids: selectedIds }),
    });

    if (!response.ok) throw new Error("Failed to delete items");
    getMenu();
  } catch (err) {
    console.log("Failed to delete items ", err);
  }
}

function resetForm() {
  itemForm.reset();
  itemIdEl.textContent = "";
  modalHeader.textContent = "Add Item";
  modal.classList.add("d-none");
}
