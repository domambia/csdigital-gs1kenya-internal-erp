$('[data-toggle="tooltip"]').tooltip('hide');
$('.toolkit > header').headroom({
	tolerance: {up: 10, down: 5},
	offset: 175,
	onUnpin: function() {
		$('.toolkit > header .yamm .dropdown.open').click();
	}
});