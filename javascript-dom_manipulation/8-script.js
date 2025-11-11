// Fetches and displays "hello" in French
// Using DOMContentLoaded to ensure the DOM is ready when script is in <head>
document.addEventListener('DOMContentLoaded', function() {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.querySelector('#hello').textContent = data.hello;
    });
});
