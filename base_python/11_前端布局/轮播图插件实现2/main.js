        var swiper1 = new Swiper('.swiper1-container', { // 区分容器
    centeredSlides: true,
    loop: true,
    autoplay: {
      delay: 2500,
      disableOnInteraction: false,
    },
    pagination: {
      el: '.swiper-p1',
      clickable: true,
    },

});
var swiper2 = new Swiper('.swiper2-container', { // 区分容器
    effect: 'fade',
    loop: true,
    centeredSlides: true,
    autoplay: {
      delay: 2500,
      disableOnInteraction: false,
    },
    pagination: {
      el: '.swiper-p2',
      clickable: true,
    },

});