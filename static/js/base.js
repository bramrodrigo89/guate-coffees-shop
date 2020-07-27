
    
// Add sticky function to navbar of base.html

function stickyContentNavbar() {
    var content_navbar = document.getElementById("content-navbar");
    var sticky = content_navbar.offsetTop;
    if (window.pageYOffset > sticky) {
        content_navbar.classList.add("stuck");
    } else {
        content_navbar.classList.remove("stuck");
    }
}

// Dismiss a toast programatically

function dismissToast() {
    var toastElement = $('.toast').first()[0];
    var toastInstance = toastElement.M_Toast;
    toastInstance.remove();
}