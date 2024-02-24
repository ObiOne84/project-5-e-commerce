$(document).ready(function () {
    // toggle between product description, reviews, and details
    $('.extra-info').on('click', function (e) {
        e.preventDefault();
        $('.extra-info').removeClass('active');
        $(this).addClass('active');

        var index = $(this).parent().index();

        $('.extra-content').removeClass('d-md-block').addClass('d-md-none');
        $('.extra-content').eq(index).removeClass('d-md-none').addClass('d-md-block');
        hideReviewForm();
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
            hideReviewForm();
        }
    });

    // Dispaly or hide overflown text
    $('.dynamic-text').on('click', function () {
        if ($(this).hasClass('overflow-hidden')) {
            $(this).removeClass('overflow-hidden');
        } else {
            $(this).addClass('overflow-hidden');
        }
    });

    // Show review from or hide if for is displayed
    $('#review-button').on('click', function () {
        showReviewForm();
    });

    // Show review from or hide if for is displayed
    $('#cancel-review').on('click', function () {
        const ScreenWidth = screen.width
        if (ScreenWidth >= 768) {
            hideReviewForm();
            $('.extra-info').last().removeClass('active');
            $('.extra-info').first().addClass('active');
            $('.extra-content').first().removeClass('d-md-none').addClass('d-md-block');
        } else {
            hideReviewForm();
        }
    });

    // Check the form for error and save in the local storage if true
    const reviewForm = document.getElementById("review-form");
    if (reviewForm) {
        reviewForm.addEventListener("submit", function () {

            const bodyInput = document.getElementById('id_body');
            const hasError = bodyInput.value.trim() === '';

            if (hasError) {
                localStorage.setItem("formError", "true");
            }
        });
    }

});

// ____________FUNCTIONS_________________________________________

function showReviewForm() {
    const ScreenWidth = screen.width
    if (ScreenWidth >= 768) {
        $('.extra-info').removeClass('active');
        $('.reviews-nav').addClass('active');
        $('.extra-content').addClass('d-md-none');
        $('#review-form-container').removeClass('d-none').addClass('d-block');
    } else {
        $('.collapse').removeClass('show');
        $('.collapse-link').removeClass('active');
        $('#review-form-container').removeClass('d-none').addClass('d-block');
    }
}

function hideReviewForm() {
    if ($('#review-form-container').hasClass('d-block')) {
        $('#review-form-container').removeClass('d-block').addClass('d-none');
    }
}

// Checking for form errors saved in the storage
document.addEventListener("DOMContentLoaded", function () {
    // Check if there's an error stored in local storage
    const showError = localStorage.getItem("formError");
    if (showError) {
        showReviewForm();
        localStorage.removeItem("formError");
    }
});