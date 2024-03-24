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
        $('html, body').animate({
            scrollTop: $('#collapseNewsletter').offset().top
        }, 500); // Adjust the duration as needed
    });

    $('#mc-embedded-subscribe-form').submit(function(event) {
        event.preventDefault(); // Prevent default form submission
        var form = $(this);
        
        $.ajax({
            type: form.attr('method'),
            url: form.attr('action'),
            data: form.serialize(),
            success: function(response) {
                // If submission is successful, collapse the newsletter section
                $('#collapseNewsletter').collapse('hide');
                // Optionally, you can display a success message or perform any other action
            },
            error: function(err) {
                // Handle errors if needed
                console.log('Error:', err);
            }
        });
    });

    $('footer').mouseenter(function () {
        $('.newsletter').slideDown();
    });

    // $('footer').mouseleave(function () {
    //     $('.newsletter').slideUp();
    // });
    $('footer').mouseleave(function () {
        setTimeout(function() {
            $('.newsletter').slideUp();
        }, 15000); // 15 seconds delay
    });

})