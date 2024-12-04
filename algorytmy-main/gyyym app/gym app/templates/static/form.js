document.getElementById('form-group').addEventListener('submit', (e) => {
  e.preventDefault();

  const formData = new FormData(e.target);
  const data = Array.from(formData.entries()).reduce((memo, [key, value]) => ({
    ...memo,
    [key]: value,
  }), {});
  document.getElementById('output').innerHTML = JSON.stringify(data);
})
  const fs = require('fs')
  let user = JSON.stringify(data);
  fs.writeFile('/users.json', user, (err) => {

    // In case of a error throw err.
    if (err) throw err;
});