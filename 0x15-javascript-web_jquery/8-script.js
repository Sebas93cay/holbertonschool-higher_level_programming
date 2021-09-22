$.ajax({
  type: 'GET',
  dataType: 'json',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: data => {
    $.each(data.results, (i, movie) => {
      $('#list_movies').append(`<li>${movie.title}</li>`);
    });
  }
});
