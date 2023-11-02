const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(URL, function (data, status) {
	if (status === 'success') {
		data.results.map((el) => {
			$('UL#list_movies').append(`<li>${el.title}</li>`);
		});
	}
});
