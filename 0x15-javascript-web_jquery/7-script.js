$.ajax({
  type: 'GET',
  dataType: 'json',
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: (data) => {
    $('#character').html(data.name);
  }
});
