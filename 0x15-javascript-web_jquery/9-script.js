// DIV#hello
const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
	$.get(URL, function (data, status) {
		if (status === 'success') {
			$('DIV#hello').text(data.hello);
		}
	});
});
