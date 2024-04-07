$(document).on('ready', function () {
	var db = new Object();
	db.preLoad = function () {
		$('.page-loader').delay(500).fadeOut(300, function () {
			$('body').fadeIn();
		});
		// navbar icon
		$('.menu-mobile-icon').click(function() {
			$('body').toggleClass("open-menu");
			const mobileMenu = $('.menu-mobile');
		});
			//accordion
			$('.faq-accordion .item .cap').click(function () {
				var content = $(this).next();
				if ($(content).is(":visible")) {
					$(this).parent().removeClass("active");
				}
				else {
					$(this).parent().addClass("active");
				}
			});
	}
	$(".tab-link").click(function() {
		var tabId = $(this).attr("data-tab");
	
		$(".tab-link").removeClass("current");
		$(".tab-content").removeClass("current");
	
		$(this).addClass("current");
		$("#" + tabId).addClass("current");
	  });
	  $('.comment-carousel .owl-carousel').owlCarousel({
		loop: true,
		margin: 10,
		responsiveClass: true,
		responsive: {
		  0: {
			items: 1,
			nav: true,
			dots: true,
		  },
		  600: {
			items: 1,
			nav: false,
			dots: true,
		  },
		  1000: {
			items: 2,
			nav: true,
			loop: false,
			dots: true,
			margin: 20
		  }
		}
	  })
	  $(".count").each(function () {
		$(this)
		  .prop("Counter", 0)
		  .animate(
			{
			  Counter: $(this).text(),
			},
			{
			  duration: 4000,
			  easing: "swing",
			  step: function (now) {
				now = Number(Math.ceil(now)).toLocaleString('en');
									  $(this).text(now);
			  },
			}
		  );
	  });


		//industry  carousel
		if ($('.owl-industry').length) {
			$('.owl-industry').owlCarousel({
				loop: true,
				margin: 20,
				items: 1,
				nav: true,
				navText: [
					'<svg class="prev-slide" width="28" height="23" viewBox="0 0 28 23" fill="none" xmlns="http://www.w3.org/2000/svg">' +
					'<path d="M26.3838 10.9014H1.46071" stroke="#015696" stroke-width="1.5" stroke-linecap="round"/>' +
					'<path d="M9.21484 2.31689L1.18407 10.9015L9.21484 20.3169" stroke="#015696" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>' +
					'</svg>',
					'<svg class="next-slide" width="28" height="23" viewBox="0 0 28 23" fill="none" xmlns="http://www.w3.org/2000/svg">' +
					'<path d="M1.61621 10.9014H26.5393" stroke="#015696" stroke-width="1.5" stroke-linecap="round"/>' +
					'<path d="M18.7852 2.31689L26.8159 10.9015L18.7852 20.3169" stroke="#015696" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>' +
					'</svg>'
				],
				responsive: {
					0: {
						items: 1,
						nav: true,
					},
					992: {
						items: 2,
						margin: 20,
						nav: true,
						center: false
					},
					1200: {
						items: 3,
						margin: 30,
						nav: true,
					}
				}
			});
		}
		$('.blog-details-carousel .owl-carousel').owlCarousel({
			loop: true,
			margin: 10,
			responsiveClass: true,
			responsive: {
			  0: {
				items: 1,
				nav: true,
				dots: true,
			  },
			  600: {
				items: 1,
				nav: false,
				dots: true,
			  },
			  1000: {
				items: 3,
				nav: true,
				loop: false,
				dots: true,
				margin: 20
			  }
			}
		  })
		// interest check 
		$('.interest-item .item input[type="checkbox"]').on('change', function() {
            var item = $(this).closest('.item');
            if ($(this).is(':checked')) {
                item.addClass('checked');
            } else {
                item.removeClass('checked');
            }
        });
		$('.how-it-work-hero .primary-button').click(function() {
            $('.choose-plan').get(0).scrollIntoView({
                behavior: 'smooth'
            });
        });
	db.preLoad();

});