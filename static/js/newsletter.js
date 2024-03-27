/*jshint esversion: 6 */
/* globals $, jQuery, ftypes, fnames */

// Chimpmail service script
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
    // Update the page date
    $('#copyright').text(new Date().getFullYear());

    // Toggle the newsletter div
    $('#newsletterToggle').click(function () {
        var maxScrollHeight = $(document).height() - $(window).height();
        $('#collapseNewsletter').collapse('show');
        window.scrollTo(0, maxScrollHeight);
        setTimeout(function () {
            $('#collapseNewsletter').collapse('hide');
        }, 30000);
    });

    if ($(window).width() > 996) {
        $('footer').mouseenter(function () {
            $('.newsletter').slideDown();
        });
        $('footer').mouseleave(function () {
            setTimeout(function () {
                $('.newsletter').slideUp();
            }, 15000);
        });
    } else {
        $('footer').click(function (event) {
            if (!$(event.target).closest('#collapseNewsletter').length &&
                !$(event.target).hasClass('footer-link')) {
                $('#collapseNewsletter').collapse('toggle');
            }
        });
    }
});