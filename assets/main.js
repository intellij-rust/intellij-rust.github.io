(function () {
    var wrap = function (fn) {
        return function (obj, func) {
            return fn.call(obj, func);
        };
    };

    var each = wrap(Array.prototype.forEach);
    var filter = wrap(Array.prototype.filter);

    /*
     * Menu
     */
    var menuBtn = document.querySelector(".menu-icon");
    if (menuBtn) {
        menuBtn.addEventListener("click", function (e) {
            e.preventDefault();
        });
    }

    /*
     * Install button
     */
    var installBtn = document.getElementById("download-stable");
    if (installBtn) {
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
    }

    /*
     * Documentation table of contents
     */
    var docNavCurrentLink = filter(document.querySelectorAll(".doc-nav > ul > li > a"), function (link) {
        return link.href == window.location.href;
    })[0];
    if (docNavCurrentLink) {
        var ul = document.createElement("ul");
        each(document.querySelectorAll(".doc > .doc-content > h2 > i"), function (anchorNode) {
            var tag = anchorNode.id,
                title = anchorNode.nextSibling.nodeValue;

            var li = document.createElement("li"),
                a = document.createElement("a");

            a.appendChild(document.createTextNode(title));
            a.title = title;
            a.href = "#" + tag;

            li.appendChild(a);
            ul.appendChild(li);
        });
        docNavCurrentLink.parentNode.appendChild(ul);
    }
})();
