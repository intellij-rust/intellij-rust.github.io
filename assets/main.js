document.addEventListener("DOMContentLoaded", function () {
    var installBtn = document.getElementById("download-stable");
    var installPane = document.getElementById("install-pane");

    installBtn.addEventListener("click", function (e) {
        installPane.classList.toggle("visible");
        e.target.blur();
        e.preventDefault()
    })
});
