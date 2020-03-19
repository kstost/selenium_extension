{
    alert = console.log;
    let finish;
    try { finish = arguments[0]; } catch{ finish = console.log; }
    return (function () {
        //----------------------------------------
        let awaiting = (ck, timeout) => {
            let refresh = 10;
            let start = performance.now();
            if (timeout === undefined) {
                timeout = -1;
            }
            return new Promise(rr => {
                (async () => {
                    let rtn;
                    let _timeout = false;
                    while (true) {
                        _timeout = (((performance.now() - start) > timeout) && timeout > 0);
                        if (_timeout || await new Promise(r => {
                            setTimeout(() => { rtn = ck(); r(rtn ? true : false); }, refresh);
                        })) { break; }
                    }
                    if (_timeout) {
                        rr();
                    } else {
                        rr(rtn);
                    }
                })();
            });
        };
        //----------------------------------------
        (['#:code:#']);
    })();
}