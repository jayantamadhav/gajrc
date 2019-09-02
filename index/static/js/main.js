
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
	$('#leave-comment').on('click',function(){
		$('comment-container').slideToggle('slow');
		$('thankyou-container').html("<div class=\'is-notification is-primary\'>Thank you for you feedback</div>");
	});
});

