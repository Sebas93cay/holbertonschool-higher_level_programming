const item = '<li>Item</li>';
window.onload = () => {
  const list = $('.my_list');
  $('#add_item').on('click', () => {
    list.append(item);
  });
  $('#clear_list').on('click', () => {
    list.html('');
  });
  $('#remove_item').on('click', () => {
    const lastItem = list.children()[list.children().length - 1];
    lastItem.remove();
  });
};
