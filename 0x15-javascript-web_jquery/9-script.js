const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.ajax({
	type: 'GET',
	url: url,
	success: function(data) {
		$('DIV#hello').text(data['hello']);
	}
});
