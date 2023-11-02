const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(URL, function (data, status) {
	if (status === 'success') {
		$('DIV#character').append(`<p>${data.name}</p>`);
	}
});
