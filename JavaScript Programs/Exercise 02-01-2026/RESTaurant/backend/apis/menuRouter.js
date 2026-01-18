const express = require("express");
const router = express.Router();

const {
  get_menu,
  add_item,
  edit_item,
  get_item,
  delete_item,
  bulk_delete_items,
} = require("./menuController");
const path = require("path");

const multer = require("multer");

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "data/images");
  },
  filename: (req, file, cb) => {
    const uniqueName =
      Date.now() +
      "-" +
      Math.round(Math.random() * 1e9) +
      path.extname(file.originalname);

    cb(null, uniqueName);
  },
});

const upload = multer({ storage });

router.get("/get-menu", get_menu);
router.post("/add-item", upload.single("image"), add_item);
router.put("/edit-item/:id", upload.single("image"), edit_item);
router.get("/get-menu/:id", get_item);
router.delete("/delete-item/:id", delete_item);
router.delete("/bulk-delete", bulk_delete_items);

module.exports = router;
