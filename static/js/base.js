// Options for dropdown button My Account from base.html

// $('.dropdown-button').dropdown({
//     inDuration: 300,
//     outDuration: 225,
//     constrainWidth: true, 
//     hover: false, 
//     gutter: 0, // Spacing from edge
//     belowOrigin: true, // Displays dropdown below the button
//     alignment: 'left', // Displays dropdown with edge aligned to the left of button
//     stopPropagation: true 
// });


// $('#mobile-account-dropdown-button').on('click',function(){
//     $('#mobile-dropdown-account').toggle();
//     console.log('i came here')
// })

// function toggleMenu(id) {
//     var menu = document.getElementById(id);
//     if (menu.style.display == 'block' || menu.style.display=='') {
//         menu.style.display = 'none';
//     } else {
//         menu.style.display = 'block';
//     }
// }
    
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

// Toast with custom HTML for messages

function createToast(message){
    var toastHTML = 
        `<span> ${message} </span>
        <button class="btn-flat toast-action">Done</button>`;
    Materialize.toast(toastHTML,10000);
}