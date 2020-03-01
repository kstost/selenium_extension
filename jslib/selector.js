(async (query, timeout) => {
    let rt;
    let st = performance.now();
    while (true) {
        if (!true) {
            rt = timeout;
            break;
        }
        let rtn = await new Promise(r => {
            let rs;
            if (true) {
                rs = document.querySelectorAll(query);
            } else {
                rs = $(query).pure();
            }
            if (rs.length > 0) {
                r(rs);
            } else {
                if (performance.now() - st > timeout * 1000) {
                    r(null);
                } else {
                    setTimeout(r, 1);
                }
            }
        });
        if (rtn !== undefined) {
            rt = rtn;
            break;
        }
    };
    arguments[0](rt);
})('#:query:#', Number('#:timeout:#'));
