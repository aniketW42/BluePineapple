const {
  add_menu,
  readCSV,
  readCSVById,
  edit_menu,
  delete_menu,
  bulk_delete,
} = require("../database");

const get_menu = async (req, res) => {
  try {
    const data = await readCSV();
    res.status(200).json(data);
  } catch (err) {
    res.status(500).json({ error: "Failed to read menu" });
  }
};

const add_item = async (req, res) => {
  try {
    const { item_name, description, price } = req.body;
    const image = req.file.filename;
    add_menu(item_name, image, description, price);
    res.status(201).json({ message: "Item added" });
  } catch (err) {
    res.status(500).json({ error: "Server error" });
  }
};

const edit_item = async (req, res) => {
  const id = req.params.id;

  try {
    const updatedFields = {
      item_name: req.body.item_name,
      description: req.body.description,
      price: req.body.price,
    };

    if (req.file) {
      updatedFields.image = req.file.filename;
    }

    await edit_menu(id, updatedFields);

    res.status(200).json({ message: "Item updated successfully" });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Server error" });
  }
};

const get_item = async (req, res) => {
  const id = req.params.id;
  try {
    const data = await readCSVById(id);
    res.status(200).json(data);
  } catch (err) {
    res.status(500).json({ error: "Server error" });
  }
};

const delete_item = async (req, res) => {
  try {
    await delete_menu(req.params.id);
    res.status(204).send("Deleted");
  } catch (err) {
    res.status(404).send(err.message);
  }
};

const bulk_delete_items = async (req, res) => {
  try {
    const { ids } = req.body;
    if (!Array.isArray(ids) || ids.length === 0) {
      return res.status(400).json({ error: "No IDs provided" });
    }

    const deletedCount = await bulk_delete(ids);

    if (deletedCount === 0) {
      return res.status(404).json({ error: "No items found" });
    }

    res.status(200).json({
      message: "Items deleted successfully",
      deletedCount,
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Server error" });
  }
};

module.exports = {
  get_menu,
  add_item,
  edit_item,
  get_item,
  delete_item,
  bulk_delete_items,
};
