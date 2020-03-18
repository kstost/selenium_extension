let finisasdfuihaiuhf3uihui3whui3hfiuh3uifhauihi3uhiu3hfiuah3iuhiuha3uihaiu3hwfiuhw3fh;
try { finisasdfuihaiuhf3uihui3whui3hfiuh3uifhauihi3uhiu3hfiuah3iuhiuha3uihaiu3hwfiuhw3fh = arguments[0]; } catch{ finisasdfuihaiuhf3uihui3whui3hfiuh3uifhauihi3uhiu3hfiuah3iuhiuha3uihaiu3hwfiuhw3fh = console.log; }
(function(){
    let finish = finisasdfuihaiuhf3uihui3whui3hfiuh3uifhauihi3uhiu3hfiuah3iuhiuha3uihaiu3hwfiuhw3fh;
    alert = console.log;
    let awaiting = (ck, timeout) => {
        let refresh = 10;
        let start = performance.now();
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
    #:code:#
})();