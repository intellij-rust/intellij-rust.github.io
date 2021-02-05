function setupRedirects(basePath, anchorMap = {}) {
    let newLocation = basePath;
    let hash = window.location.hash.substring(1);
    if (hash) {
        let redirect = anchorMap[hash];
        if (redirect) {
            newLocation = redirect
        }
    }

    window.location.replace("https://plugins.jetbrains.com/plugin/8182-rust/docs/" + newLocation);
}
