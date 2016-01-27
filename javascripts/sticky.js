$(function(){ // document ready
  var stickyTop = $('#navigator').offset().top; // returns number
  $(window).scroll(function(){ // scroll event
    var windowTop = $(window).scrollTop(); // returns number
    if (stickyTop < windowTop) {
      $('#navigator').css({ position: 'fixed', top: 0 });
    }
    else {
      $('#navigator').css('position','static');
    }
  });
});
