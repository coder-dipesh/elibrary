$(document).ready(function () {
  $("#owl-demo").owlCarousel({
    loop: true,
    margin: 10,
    nav: false,
    autoplayHoverPause: true,
    autoplay: true,
    autoplayTimeout: 3000,

    responsive: {
      0: {
        items: 2,
      },
      600: {
        items: 3,
      },
      1000: {
        items: 4,
      },
    },
  });
});
