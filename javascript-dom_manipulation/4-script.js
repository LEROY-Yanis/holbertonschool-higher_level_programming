// Adds a li element to the list when clicking on add_item
document.querySelector('#add_item').addEventListener('click', function() {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newItem);
});
