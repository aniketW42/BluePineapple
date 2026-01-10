const axios = require("axios");

async function getPostsAndComments() {
  try {
    const [postsRes, commentsRes] = await Promise.all([
      axios.get("https://jsonplaceholder.typicode.com/posts"),
      axios.get("https://jsonplaceholder.typicode.com/comments"),
    ]); // waiting for both posts and comments using Promise.all

    console.log("Posts:", postsRes.data[0]); 
    console.log("Comments:", commentsRes.data[0]);
  } catch (err) {
    console.error("Error fetching data:", err.message);
  }
}

getPostsAndComments();
