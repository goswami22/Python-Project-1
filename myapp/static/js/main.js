$(document).ready(function () {
    // navbar js
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.navbar').addClass('nav-animation')
        } else {
            $('.navbar').removeClass('nav-animation')
        }
    });
    // banner js
    $('.hero-banner').owlCarousel({
        loop: true,
        margin: 0,
        animateOut: 'fadeOut',
        nav: false,
        dots: true,
        responsive: {
            0: {
                items: 1
            }
        }
    })

    // block content slider
    $('.block-content-slider').owlCarousel({
        loop: true,
        margin: 5,
        nav: false,
        dots: false,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 3
            },
            1200: {
                items: 4
            },
            1600: {
                items: 5
            }
        }
    })

    // category feature slider
    $('.category-feature-slider').owlCarousel({
        loop: true,
        margin: 0,
        nav: false,
        dots: false,
        responsive: {
            0: {
                items: 1,
                autoplay: true,
                autoplayTimeout: 6000,
                autoplaySpeed: 3000,
            },
            768: {
                items: 2,
            },
            1200: {
                items: 4,
                autoplay: false,
            },
            1600: {
                items: 5
            }
        }
    })

    // Main product left slider
    $('.main-product-slider').owlCarousel({
        loop: true,
        margin: 0,
        nav: true,
        dots: false,
        items: 1,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 1
            }
        }
    })

    // Main product left slider
    $('.main-product-right-slider').owlCarousel({
        loop: true,
        margin: 0,
        nav: true,
        dots: false,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 3
            },
            1200: {
                items: 4
            },
            1500: {
                items: 5
            }
        }
    })

    // best seller slider
    $('.best-seller-slider').owlCarousel({
        loop: true,
        margin: 0,
        nav: true,
        autoplay: true,
        autoplayTimeout: 6000,
        autoplaySpeed: 3000,
        dots: false,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2,
                nav: true,
            },
            1200: {
                items: 3,
            },
            1600: {
                items: 4,
            }
        }
    })

    // best news slider
    $('.best-news-slider').owlCarousel({
        loop: true,
        margin: 30,
        nav: true,
        dots: false,
        responsive: {
            0: {
                items: 1,
            },
            768: {
                items: 2,
            },
            1200: {
                items: 3,
            },
            1600: {
                items: 4,
            }
        }
    })

    // partner slider
    $('.partner-slider').owlCarousel({
        loop: true,
        margin: 30,
        autoplay: true,
        slideTransition: 'linear',
        autoplayTimeout: 3000,
        autoplaySpeed: 3000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 2
            },
            768: {
                items: 4
            },
            1200: {
                items: 5
            }
        }
    })
    // partner slider
    $('.partner-slider').owlCarousel({
        loop: true,
        margin: 30,
        autoplay: true,
        slideTransition: 'linear',
        autoplayTimeout: 3000,
        autoplaySpeed: 3000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 4
            },
            1200: {
                items: 5
            }
        }
    })
    // cms banner slider
    if ($(window).width() < 767) {
        $('.cms-banner-wrapper').owlCarousel({
            loop: true,
            margin: 30,
            nav: false,
            dots: false,
            autoplay: true,
            autoplayTimeout: 4000,
            autoplaySpeed: 4000,
            responsive: {
                0: {
                    items: 1
                },
                768: {
                    items: 1
                }
            }
        })
    }

    // footer & filter category
    $('footer h5.accordion-title, .filter-area .single-filter:first-child .single-filter-header').click(function () {
        $(this).next().slideToggle();
        $(this).toggleClass('active');
    });


    // filter menu
    $('.mobile-filter .single-filter .single-filter-header').click(function () {
        $(this).next().addClass('active');
    })
    $('.mobile-filter .single-filter .filter-menu-header').click(function () {
        $(this).parent().removeClass('active')
    })

    // about services slider
    $('.about-services-silder').owlCarousel({
        loop: false,
        margin: 30,
        autoplay: true,
        autoplayTimeout: 4000,
        autoplaySpeed: 3000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            1200: {
                items: 3
            }
        }
    })
    // blog slider
    $('.blog-silder').owlCarousel({
        loop: false,
        margin: 30,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplaySpeed: 6000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            400: {
                items: 2
            },
            768: {
                items: 2
            },
            1200: {
                items: 3
            }
        }
    })
    // blog slider
    $('.related-product-slider').owlCarousel({
        loop: false,
        margin: 30,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplaySpeed: 6000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            400: {vertical: true,
                items: 2
            },
            768: {
                items: 4
            },
            1200: {
                items: 6
            }
        }
    })
    // our team silder
    $('.our-team-silder').owlCarousel({
        loop: false,
        margin: 30,
        dots: false,
        nav: true,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplaySpeed: 6000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            400: {
                items: 2
            },
            768: {
                items: 3
            },
            1200: {
                items: 5
            }
        }
    })

    // number counting
    $('.count').prop('disabled', true);
    $(document).on('click', '.plus', function () {
        $('.count').val(parseInt($('.count').val()) + 1);
    });
    $(document).on('click', '.minus', function () {
        $('.count').val(parseInt($('.count').val()) - 1);
        if ($('.count').val() == 0) {
            $('.count').val(1);
        }
    });

    // product detail js
    $('.product-slider.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav',
        loop:false
    });
    $('.product-slider.slider-nav').slick({
        slidesToShow: 4, // 3,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        dots: false,
        nav: true,
        arrows:true,
        focusOnSelect: true,
        vertical: true,
        loop: false,
    });

    // review 
    $('.review-btn-area a').on('click', function(){
        $('.review-content').slideToggle()
    })

 
})
