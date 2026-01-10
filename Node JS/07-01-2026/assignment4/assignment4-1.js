async function fetchData() {
  try {
    await new Promise((resolve) => {
      setTimeout(resolve, 2000); //api delay
    });
    return "Data fetched successfully"; //success
  } catch (err) {
    return err; //failure
  }
}

fetchData()
  .then((message) => console.log(message))
  .catch((error) => console.error(error.message));
