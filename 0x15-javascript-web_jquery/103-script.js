window.onload = () => {
  const translateButton = $('#btn_translate');
  translateButton.on('click', translateHello);
};

const translateHello = () => {
  const langCode = $('#language_code').val();
  $.ajax({
    type: 'POST',
    dataType: 'json',
    url: `https://fourtonfish.com/hellosalut/?lang=${langCode}`,
    success: data => {
      $('#hello').html(data.hello);
    }
  });
};
