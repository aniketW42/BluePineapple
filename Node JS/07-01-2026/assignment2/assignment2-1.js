const fs = require("fs/promises");

fs.writeFile("./log.txt", "This is a log file.", { flag: "a" }) // writing file using append mode
  .then(console.log("File created and written successfully. "))
  .catch((err) => {
    console.log(err);
  });
