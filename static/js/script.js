window.onscroll = function() {
    stickyNavbar();
};

var navbar = document.getElementById("navbar");
var navbarPlaceholder = document.getElementById("navbar-placeholder")
var sticky = navbar.offsetTop;

function stickyNavbar() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky");
        navbarPlaceholder.style.height = "120px"
    } else {
        navbar.classList.remove("sticky");
        navbarPlaceholder.style.height = "60px"
    }
}
