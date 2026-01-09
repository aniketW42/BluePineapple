const { add_menu, readCSV, readCSVById, edit_menu, delete_menu } = require('../database');

const get_menu = async (req, res) => {
    try {
        const data = await readCSV();  
        res.status(200).json(data);    
    } catch (err) {
        res.status(500).json({ error: "Failed to read menu" });
    }
};

const add_item = async (req, res) =>{

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
            price: req.body.price
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


const get_item = async (req, res) =>{

    const id = req.params.id;

    try {
        const data = await readCSVById(id)
        res.status(200).json(data);
    } catch (err){
        res.status(500).json({ error: "Server error" });
    }   

};

const delete_item =  async (req, res) =>{
    const id = req.params.id;
    try{
        delete_menu(id)
    }catch (err){
        res.status(500).json({ error: "Server error" });
    }   
}

module.exports = {
    get_menu, add_item, edit_item, get_item, delete_item
}