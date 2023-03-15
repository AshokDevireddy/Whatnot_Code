const form = document.querySelector('form');
form.addEventListener('submit', e => {
  e.preventDefault();
  const formData = new FormData(form);
  fetch('/upload', {
    method: 'POST',
    body: formData
  })
  .then(response => response.text())
  .then(result => {
    const output = document.getElementById('result');
    output.innerHTML = result;
  });
});
