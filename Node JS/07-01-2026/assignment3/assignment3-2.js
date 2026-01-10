function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const success = true;

            if (success) {
                resolve("Data fetched successfully"); //success
            } else { 
                reject("Error: Failed to fetch data"); //failure
            }
        }, 2000); //api delay
    });
}

fetchData()
    .then((message) => console.log(message))
    .catch((error) => console.error(error));

// if success = true --> Data fetched successfully
// else success = false --> Error: Failed to fetch data