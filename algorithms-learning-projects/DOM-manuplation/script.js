const responseDiv = document.getElementById('response');
const form = document.getElementById('form');

form.addEventListener('submit', e => {
  e.preventDefault();

  const username = document.getElementById('username').value.trim();
  const email = document.getElementById('email').value.trim();

  axios.post("https://jsonplaceholder.typicode.com/posts/", {
      username: username,
      email: email
    })
    .then(res => {
      const data = res.data;
      responseDiv.innerHTML = `
        <h2>Response Data</h2>
        <p><b>User Name:</b> ${data.username}</p>
        <p><b>Email:</b> ${data.email}</p>
      `;
    })
    .catch(error => {
      console.error(error.message);
      responseDiv.innerHTML = "<b style='color:red;'>Please try again. Network error.</b>";
    });
});
