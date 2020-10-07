
    
// Add sticky function to navbar of base.html
// Source: https://www.w3schools.com/howto/howto_js_sticky_header.asp

function stickyContentNavbar() {
    if (window.pageYOffset > sticky) {
        contentNavbar.classList.add("stuck");
    } else {
        contentNavbar.classList.remove("stuck");
    }
}

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

// Dismiss a toast programatically

function dismissToast() {
    var toastElement = $('.toast').first()[0];
    var toastInstance = toastElement.M_Toast;
    toastInstance.remove();
}

// Start AutoPlay for Carousel items or Carousel Sliders

function autoplay() {
    $('.carousel').carousel('next');
    setTimeout(autoplay, 4500);
}