$(document).ready(function () {
    // toggle between product description, reviews, and details
    $('.extra-info').on('click', function (e) {
        e.preventDefault();
        $('.extra-info').removeClass('active');
        $(this).addClass('active');

        var index = $(this).parent().index();

        $('.extra-content').removeClass('d-md-block').addClass('d-md-none');
        $('.extra-content').eq(index).removeClass('d-md-none').addClass('d-md-block');
    });

    // Display truncated text
    $('.truncated-text').on('click', function () {
        $(this).toggleClass('expanded');
    });

    function expandText(element) {
        element.classList.toggle('expanded');
    }

    // Add and remove active class for mobile device when toggle
    $('.collapse-link').on('click', function () {
        if ($(this).hasClass('active')) {
            $(this).removeClass('active');
        } else {
            $(this).addClass('active');
        }
    });

});