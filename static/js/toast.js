
var toastElement = document.querySelector('.toast');
var toast = new bootstrap.Toast(toastElement);
toast.show();

startTime = new Date();

setInterval(updateTime, 1000);

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

    if (elapsedTime >= 150) {
        toast.hide();
    }
}