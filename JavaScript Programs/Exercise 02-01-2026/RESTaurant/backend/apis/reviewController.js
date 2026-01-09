
const express = require('express');
const router = express.Router();
const multer = require('multer');
const path = require("path");

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, "data/gallery");
    },
    filename: (req, file, cb) => {
        const uniqueName =
            Date.now() + "-" + Math.round(Math.random() * 1E9) +
            path.extname(file.originalname);

        cb(null, uniqueName);
    }
});

const upload = multer({ storage });

router.post('/add-review', upload.single('image'), (req, res)=>{
    console.log(req.file.filename)
    if (req.file) {
        console.log('File received:', req.file.originalname);
        res.status(200).json({
        message: 'File uploaded successfully',
        filename: req.file.originalname
        });
    } else {
        res.status(400).send('No file uploaded!');
    }
});

module.exports = router