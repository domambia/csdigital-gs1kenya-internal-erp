$(document).on('click', '.yamm .dropdown-menu', function(e) {
	e.stopPropagation()
});

$(document).on('click', '.yamm .dropdown-menu a', function(e) {
	// Dismisses the mega menu when an in-page link is clicked.
	// TODO: only dismiss the menu when link is clicked for the current page.
	if ($(e.target).attr('href').indexOf('#') != -1) {
		$(e.target).parents('.open').click();
	}
});