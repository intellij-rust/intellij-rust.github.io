$(function () {
    /*
     * Menu
     */
    $(".menu-icon").on("click", function (e) {
        e.preventDefault();
    });

    /*
     * Install button
     */
    $("#download-stable").each(function () {
        var installPane = $("#install-pane");
        var installPaneCloseBtn = $("#install-pane-close");

        $(this).on("click", function (e) {
            installPane.toggleClass("visible");
            $(e.target).blur();
            e.preventDefault();
        });

        installPaneCloseBtn.on("click", function (e) {
            installPane.removeClass("visible");
            e.preventDefault();
        });
    });

    /*
     * Documentation table of contents
     */
    $(".doc-nav > ul > li > a")
        .filter(function (idx, link) {
            return link.href == window.location.href
        })
        .after(function () {
            var ul = $("<ul/>");
            $(".doc > .doc-content > h2 > i").each(function () {
                var tag = $(this).attr("id"),
                    title = this.nextSibling.nodeValue;

                ul.append(
                    $("<li/>").append(
                        $("<a/>")
                            .attr("href", "#" + tag)
                            .attr("title", title)
                            .text(title)));
            });
            return ul;
        });

    /*
     * GIF Player
     */
    $(".gif").gifplayer();
});
