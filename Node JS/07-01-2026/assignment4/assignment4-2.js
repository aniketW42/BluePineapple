const axios = require("axios");

async function getPosts() {
  try {
    const response = await axios.get( 
      "https://jsonplaceholder.typicode.com/posts"
    ); // geting posts

    const posts = response.data; // extracting data from responce 
    posts.slice(0, 5).forEach((post, index) => {  // extracting only 5 posts
      console.log(`Post: ${index + 1}`);
      console.log("Title: " + post.title);
      console.log("Body: " + post.body);
      console.log("-------");
    });
  } catch (err) {
    console.error("Error fetching posts: ", err.message);
  }
}

getPosts();
