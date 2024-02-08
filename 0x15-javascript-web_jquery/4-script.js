$('DIV#toggle_header').on('click', function() {
	if ($('header').hasClass('green'))
	{
		$('header').removeClass('green')
		$('header').addClass('red')
		console.log('sucess')
	}
	else if ($('header').hasClass('red'))
	{
		$('header').removeClass('red')
		$('header').addClass('green')
	}
	
})
