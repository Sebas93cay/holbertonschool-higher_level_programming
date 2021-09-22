const header = $('header');
console.log(header);
$('#toggle_header').on('click', () => {
  console.log('clic');
  if (header.hasClass('red')) {
    header.addClass('green');
    header.removeClass('red');
  } else if (header.hasClass('green')) {
    header.addClass('red');
    header.removeClass('green');
  }
});
