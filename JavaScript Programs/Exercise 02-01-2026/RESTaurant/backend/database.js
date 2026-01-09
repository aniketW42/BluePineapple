const fs = require("fs");
const csv = require("csv-parser");
const { randomUUID } = require("crypto");

const FILE = "./data/menu.csv";

function readCSV() {
    return new Promise((resolve, reject) => {
        const results = [];

        fs.createReadStream(FILE, { encoding: "utf8" })
            .pipe(csv({
                mapHeaders: ({ header }) =>
                    header.replace(/^\uFEFF/, "").trim()
            }))
            .on("data", data => results.push(data))
            .on("end", () => resolve(results))
            .on("error", err => reject(err));
    });
}

function readCSVById(id) {
  return new Promise((resolve, reject) => {
    let found = null;
    
    fs.createReadStream(FILE, { encoding: "utf8" })
      .pipe(csv({
        mapHeaders: ({ header }) =>
          header.replace(/^\uFEFF/, "").trim()
      }))
      .on("data", (row) => {
        if (row.id == id) {
          found = row;
        }
      })
      .on("end", () => {
        resolve(found); 
      })
      .on("error", reject);
  });
}

function writeCSV(data) {
    const headers = Object.keys(data[0]).join(",");
    const rows = data.map(obj => Object.values(obj).join(","));
    const csvData = [headers, ...rows].join("\n");

    fs.writeFileSync(FILE, csvData);
}

async function add_menu(item_name, image, description, price) {
    const data = await readCSV();

    data.push({
        id : randomUUID(),
        item_name,
        image,
        description,
        price
    });
    writeCSV(data);
}

async function edit_menu(id, updatedFields) {
    const data = await readCSV();
    console.log("2" + updatedFields)
    let updated = false;

    const newData = data.map(row => {
        if (row.id == id) {
            updated = true;
            return { ...row, ...updatedFields };
        }
        return row;
    });

    if (!updated) {
        throw new Error("Item not found");
    }

    writeCSV(newData);
}

async function delete_menu(id) {
    const data = await readCSV();

    const newData = data.filter(row => row.id != id);

    if (newData.length === data.length) {
        throw new Error("Item not found");
    }

    writeCSV(newData);
}


module.exports = {
    add_menu, readCSV, readCSVById, edit_menu, delete_menu
};