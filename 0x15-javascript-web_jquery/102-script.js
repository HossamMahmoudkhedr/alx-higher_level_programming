const URL = 'https://www.fourtonfish.com/hellosalut/hello/';
$(document).ready(function () {
	let value;
	$('INPUT#language_code').change(function (e) {
		value = e.target.value;
	});

	$('INPUT#btn_translate').click(function () {
		$.get(URL, function (data, status) {
			if (status === 'success') {
				$('DIV#hello').text(data[value]);
			}
		});
	});
});
