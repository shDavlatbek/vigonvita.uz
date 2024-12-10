(function ($) {
    "use strict";
    Fancybox.bind('[data-fancybox]', {
        // Your custom options
    });    
    var swiper_photo = new Swiper("#swiper-photos", {
        slidesPerView: 'auto',
        spaceBetween: 40,
        autoplay: {
            delay: 2500,
            disableOnInteraction: false,
          },
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: true,
        loop: true,
        coverflowEffect: {
            rotate: 0,
            stretch: 0,
            depth: 120,
            modifier: 1,
            slideShadows: false,
        }
    });
})(jQuery);