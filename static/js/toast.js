/*jshint esversion: 6 */
/* globals $, bootstrap */

$(document).ready(function () {
    var toastElement = document.querySelector('.toast');

    if (toastElement !== null) {
        var toast = new bootstrap.Toast(toastElement);
        toast.show();
        toastElement.classList.add('slide-in-right');

        var startTime = new Date(); // Moved declaration here
        setInterval(updateTime, 1000);
    }

    /** Function to update the time and hide toast after set time */
    function updateTime() {
        var timeElement = document.getElementsByClassName("time")[0];
        var currentTime = new Date();
        var elapsedTime = Math.round((currentTime - startTime) / 1000);
        if (elapsedTime < 10) {
            timeElement.textContent = "Just now";
        } else {
            if (elapsedTime < 60) {
                var seconds = Math.floor(elapsedTime / 1);
                timeElement.textContent = seconds + " seconds ago";
            } else {
                var minutes = Math.floor(elapsedTime / 60);
                if (minutes === 1) {
                    timeElement.textContent = minutes + " minute ago";
                } else {
                    timeElement.textContent = minutes + " minutes ago";
                }
            }
        }

        if (elapsedTime >= 15) {
            if (toast) {
                toast.hide();
                toastElement.classList.add('slide-out-left');
            }
        }
    }
});
