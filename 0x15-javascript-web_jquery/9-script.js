$.ajax({
  type: 'GET',
  dataType: 'json',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: data => {
    $('#hello').html(data.hello);
  }
});
