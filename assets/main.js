(function () {
    var wrap = function (fn) {
        return function () {
            return fn.apply(arguments[0], Array.prototype.slice.call(arguments, 1));
        }
    };

    var each = wrap(Array.prototype.forEach);
    var filter = wrap(Array.prototype.filter);
    var map = wrap(Array.prototype.map);
    var mapNotUndef = function (obj, fn) {
        return filter(map(obj, fn), function (it) {
            return it !== undefined
        });
    };

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
            e.preventDefault()
            ;
        });

        installPaneCloseBtn.addEventListener("click", function (e) {
            installPane.classList.remove("visible"
            );
            e.preventDefault();
        });
    }

    /*
     * Documentation table of contents
     */
    var doc = document.getElementsByClassName("doc")[0];
    if (doc) {
        var docNav = document.getElementsByClassName("doc-nav")[0];
        var link = filter(docNav.getElementsByTagName("a"), function (link) {
            return link.href == window.location.href;
        })[0];

        if (!link) return;

        var headers = mapNotUndef(doc.getElementsByTagName("h2"), function (header) {
            var anchorNode = header.getElementsByTagName("i")[0];
            if (!anchorNode) return undefined;
            var textNode = anchorNode.nextSibling;
            if (!textNode) return undefined;

            return {
                tag: anchorNode.id,
                title: textNode.nodeValue
            }
        });

        var ul = document.createElement("ul");
        each(headers, function (h) {
            var li = document.createElement("li");
            var a = document.createElement("a");

            a.appendChild(document.createTextNode(h.title));
            a.title = h.title;
            a.href = "#" + h.tag;

            li.appendChild(a);
            ul.appendChild(li);
        });
        link.parentNode.appendChild(ul);
    }
})();
