
$(document).ready(function() {
	$('.loader_container').fadeOut("slow");
	$(".navbar-burger").click(function() {
		// Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
		$(".navbar-burger").toggleClass("is-active");
		$(".navbar-menu").toggleClass("is-active");
	});
	$("#comment-button").on('click', function(){
		$("i", this).toggleClass("fa-chevron-down fa-chevron-up");
		$("#comment-container").slideToggle("Slow");
	});
	$('.slider').slick({

				dots: false,
				prevArrow: false,
				nextArrow: false,
				vertical: true,
				slidesToShow: 3,
				slidesToScroll: 1,
				autoplay: true,
				infinite: true,
				autoplaySpeed: 3000,
				outerEdgeLimit: true
			});

});

