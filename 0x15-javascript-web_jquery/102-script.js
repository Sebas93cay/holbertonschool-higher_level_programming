window.onload = () => {
  $('#btn_translate').on('click', () => {
    const langCode = $('#language_code').val();
    $.ajax({
      type: 'POST',
      dataType: 'json',
      url: `https://fourtonfish.com/hellosalut/?lang=${langCode}`,
      success: data => {
        $('#hello').html(data.hello);
      }
    });
  });
};
