(function ($) {
    window.fnames = new Array();
    window.ftypes = new Array();
    fnames[0] = 'EMAIL';
    ftypes[0] = 'email';
    fnames[1] = 'FNAME';
    ftypes[1] = 'text';
    fnames[2] = 'LNAME';
    ftypes[2] = 'text';
    fnames[3] = 'ADDRESS';
    ftypes[3] = 'address';
    fnames[4] = 'PHONE';
    ftypes[4] = 'phone';
    fnames[5] = 'BIRTHDAY';
    ftypes[5] = 'birthday';
}(jQuery));
var $mcj = jQuery.noConflict(true);

$(document).ready(function () {
    $('#copyright').text(new Date().getFullYear());

    $('#newsletterToggle').click(function() {
        $('#collapseNewsletter').collapse('toggle');
    });

    $('footer').mouseenter(function () {
        $('.newsletter').slideDown();
    });

    $('footer').mouseleave(function () {
        $('.newsletter').slideUp();
    });

})