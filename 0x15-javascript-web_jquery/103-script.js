const URL = 'https://www.fourtonfish.com/hellosalut/hello/';

const FetchData = (value) => {
	$.get(URL, function (data, status) {
		if (status === 'success') {
			$('DIV#hello').text(data[value]);
		}
	});
};

$(document).ready(function () {
	let value;
	$('INPUT#language_code').change(function (e) {
		value = e.target.value;
	});

	$('INPUT#btn_translate').click(function () {
		FetchData(value);
	});

	$(window).keypress(function (e) {
		if (e.which === 13) {
			FetchData(value);
		}
	});
});
