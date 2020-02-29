(async (timeout) => {
    let st = performance.now();
    function ready() {
        return document.readyState === 'complete';
    }
    while (true) {
        if (ready()) {
            break;
        } else {
            let ad = await new Promise(r => {
                if (performance.now() - st > timeout * 1000) {
                    r(true);
                } else {
                    setTimeout(r, 10);
                }
            });
            if (ad) {
                break;
            }
        }
    };
    arguments[0](true);
})(Number('#:timeout:#'));
