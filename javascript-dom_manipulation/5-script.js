// Updates the text of the header element when clicking on update_header
document.querySelector('#update_header').addEventListener('click', function() {
  document.querySelector('header').textContent = 'New Header!!!';
});
