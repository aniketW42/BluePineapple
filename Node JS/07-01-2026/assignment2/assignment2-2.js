const fs = require("fs");

function blocking() {
  console.log("(Blocking) START");

  const data = fs.readFileSync("./log.txt", { encoding: "utf8" }); // blocking read
  console.log(data);

  console.log("(Blocking) END");
}

function nonBlocking() {
  console.log("(Non Blocking) START");

  fs.promises
    .readFile("./log.txt", { encoding: "utf8" }) // non-blocking read
    .then((data) => console.log(data))
    .catch((err) => console.error(err));

  console.log("Non Blocking) END");
}

blocking(); // output : START -> data -> END
nonBlocking(); // output : START -> END -> data
