$(document).ready(function () {
    // Return to the top
    // Source: Boutique Ado walkthrough project
    var arrowUp = $('.btt-link');
    if (arrowUp.length) {
        arrowUp.click(function (e) {
            e.preventDefault();
            window.scrollTo(0, 0);
        });
    }
});
