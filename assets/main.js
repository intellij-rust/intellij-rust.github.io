document.addEventListener("DOMContentLoaded", function () {
    var installBtn = document.getElementById("download-stable");
    var installPane = document.getElementById("install-pane");
    var installPaneCloseBtn = document.getElementById("install-pane-close");

    installBtn.addEventListener("click", function (e) {
        installPane.classList.toggle("visible");
        e.target.blur();
        e.preventDefault();
    });

    installPaneCloseBtn.addEventListener("click", function (e) {
        installPane.classList.remove("visible");
        e.preventDefault();
    });
});
